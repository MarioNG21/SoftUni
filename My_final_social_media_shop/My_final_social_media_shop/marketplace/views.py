import decimal
from datetime import datetime, date

from django.contrib import messages
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.views.generic import detail
from My_final_social_media_shop.marketplace.forms import CreationAdForm, EditAdForm, DeleteAdForm, CheckOutForm, \
    PaymentForm, CategoryAddForm, CategoryEditForm, CategoryDeleteForm
from My_final_social_media_shop.marketplace.models import Product, OrderItem, Order, Category, BillingAddress


class ShowHome(views.TemplateView):
    template_name = 'home.html'


class MarketplaceView(views.ListView):
    model = Product
    template_name = 'marketplace.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        if 'slug' in self.kwargs or 'slug' in self.request.GET:
            qs = super().get_queryset()
            slug = ''
            if 'slug' in self.kwargs:
                slug = self.kwargs['slug']
            elif 'slug' in self.request.GET:
                slug = self.request.GET['slug']

            return qs.filter(category__slug__icontains=slug)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreateAdvertisement(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'create_ad.html'
    form_class = CreationAdForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditAdvertisementView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'edit_ad.html'
    model = Product
    form_class = EditAdForm

    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            return reverse('product details', kwargs={'pk': pk})

        return reverse_lazy('marketplace')


class DeleteAdvertisementView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'delete_ad.html'
    model = Product
    form_class = DeleteAdForm
    success_url = reverse_lazy('marketplace')


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'ad_details.html'
    success_url = reverse_lazy('market')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user

        return context


class CartView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'cart_detail.html'
    model = OrderItem
    context_object_name = 'order_items'
    ordering = '-id'

    def get_queryset(self):
        result = super().get_queryset().filter(user=self.request.user)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        qnt = 0

        for item in self.object_list:
            qnt += item.quantity
            total += (item.product.price * item.quantity)

            tax = total * decimal.Decimal(
                0.02)  # because price is decimal-field and 0.02 is float : float approximately value and decimal store fix values
            context['total'] = total
            context['qnt'] = qnt
            context['tax'] = tax
            context['tax_plus_total'] = tax + total
        return context


class AddingObjectView(auth_mixins.LoginRequiredMixin, detail.BaseDetailView):
    def get(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        product = Product.objects.get(id=pk)
        ordered_item, created = OrderItem.objects.get_or_create(
            product=product,

            user=self.request.user
        )

        order_qs = Order.objects.filter(
            user=self.request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs.get()
            if order.items.filter(product_id=product.pk):
                ordered_item.quantity += 1
                ordered_item.save()
                messages.info(self.request, 'This item quantity was updated plus 1!')
            else:
                order.items.add(ordered_item)
                messages.info(self.request, 'This item was added to your cart! ')

        else:
            order = Order.objects.create(user=self.request.user)
            order.items.add(ordered_item)
            messages.info(self.request, 'New order was created successfully!')

        return redirect(reverse_lazy('product details', kwargs={'pk': product.pk}))


@login_required
def remove_product_from_order(request, pk):
    selected_product = Product.objects.filter(pk=pk).get()
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.get()
        if order.items.filter(product_id=selected_product.pk):
            ordered_item = OrderItem.objects.filter(
                product_id=pk,

            ).get()
            messages.info(request, "This item was successfully removed from your order ")
            order.items.remove(ordered_item)
            OrderItem.objects.filter(
                product_id=pk,

            ).delete()

            return redirect(reverse_lazy('cart'))
        else:
            messages.info(request, 'This item does not exists in your cart')
            return redirect(reverse_lazy('cart'))

    else:
        messages.info(request, 'There is no order which has been made !')
        return redirect(reverse_lazy('cart'))


@login_required
def add_view(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    order_item.quantity += 1
    order_item.save()
    messages.info(request, 'This item quantity was updated plus 1!')
    return redirect('cart')


@login_required
def remove_view(request, pk):
    order_item = OrderItem.objects.get(pk=pk)

    order_item.quantity -= 1
    if order_item.quantity <= 0:
        order_item.delete()
        messages.info(request, 'This item was removed!')
    else:

        order_item.save()
        messages.info(request, 'This item quantity was updated minus 1!')
    return redirect('cart')


class CheckOutView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'checkout-page.html'
    success_url = reverse_lazy('marketplace')
    form_class = CheckOutForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            order_items_user = OrderItem.objects.filter(user=context['form'].user)
            context['object_list'] = order_items_user
            context['has_items'] = True
        except ObjectDoesNotExist:
            pass
        context['has_order'] = Order.objects.filter(user=self.request.user).exists()
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        if self.request.method == 'POST':
            try:
                user = form.user
                order = Order.objects.get(user=user, ordered=False)
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                address = form.cleaned_data['address']
                country = form.cleaned_data['country']
                zip = form.cleaned_data['zip']
                state = form.cleaned_data['state']
                phone = form.cleaned_data['phone']

                billing_address, created = BillingAddress.objects.get_or_create(
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    country=country,
                    zip=zip,
                    state=state,
                    phone=phone,
                    user=user,

                )
                if created:
                    billing_qs = BillingAddress.objects.filter(user=user)
                    if billing_qs.exists():
                        BillingAddress.objects.filter(user=user).delete()
                    billing_address.save()

                    order.billing_address = billing_address
                    order.save()
                # Should redirect to payment
                result.headers['Location'] = reverse_lazy('payment')
            except ObjectDoesNotExist:
                messages.info(self.request, 'There is problem with your billing address, check it again')
                result.headers['Location'] = reverse_lazy('checkout')

        return result


class PaymentView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'payment.html'
    success_url = reverse_lazy('marketplace')
    form_class = PaymentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = context['form'].user
            order_items_user = OrderItem.objects.filter(user=user)
            billing_qs = user.billingaddress_set.filter(user=user)
            billing_address = billing_qs.last()
            context['billing_address'] = billing_address
            context['object_list'] = order_items_user
            total = 0
            qnt = 0

            for item in order_items_user:
                qnt += item.quantity
                total += (item.product.price * item.quantity)

            tax = total * decimal.Decimal(
                0.02)  # because price is decimal-field and 0.02 is float : float approximately value and decimal store fix values
            context['total'] = total
            context['qnt'] = qnt
            context['tax'] = tax
            context['tax_plus_total'] = tax + total
        except ObjectDoesNotExist:
            pass
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        if self.request.method == 'POST':
            order_qs = Order.objects.filter(user=form.user, ordered=False)
            if order_qs.exists():
                order = order_qs.get()
                order.ordered = True
                order.date_send_on = date.today()
                order.save()
                order_items = OrderItem.objects.filter(user=form.user).delete()

                result.headers['Location'] = reverse_lazy('after-payment') + '?command=successfullypaid'
            else:
                result.headers['Location'] = reverse_lazy('after-payment') + '?command=unsuccessfullypaid'
        return result


class AfterPaymentView(views.TemplateView):
    template_name = 'after_payment.html'


class CategoryCreateView(views.CreateView):
    form_class = CategoryAddForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('index')


class CategoryEditView(views.UpdateView):
    form_class = CategoryEditForm
    model = Category
    template_name = 'edit_category.html'
    success_url = reverse_lazy('index')


class CategoryDeleteView(views.DeleteView):
    template_name = 'delete_category.html'
    model = Product
    form_class = CategoryDeleteForm
    success_url = reverse_lazy('index')
