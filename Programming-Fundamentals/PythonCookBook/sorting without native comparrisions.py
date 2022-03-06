import os

filenames = os.listdir('.')
[name for name in filenames if name.endswith(('.c', '.h'))]