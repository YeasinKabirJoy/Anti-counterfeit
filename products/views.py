from django.shortcuts import render
from .models import Carton,Product
from .addProductForm import AddCartonAndProductForm
from. keys import encrypt_box,decrypt_box

import qrcode
# Create your views here.
def add_carton(request):
    form = AddCartonAndProductForm
    if request.method == 'POST':
        form = AddCartonAndProductForm(request.POST)
        if form.is_valid():
            form.save()
            quantity = request.POST['quantity']
            cid= request.POST['cid']
            encrypted_carton_id =encrypt_box.encrypt(cid)
            img = qrcode.make(encrypted_carton_id)
            img.save("{}.png".format(cid))
            for i in range(1,quantity+1):
                if i < 10:
                    pid = cid+'p00'+str(i)
                elif i > 9 and i < 100:
                    pid = cid + 'p0' + str(i)
                else:
                    pid = cid + 'p' + str(i)

                encrypted_product_id = encrypt_box.encrypt(pid)

                product= Product(product_id=pid,carton_id=cid)
                product.save()
                img = qrcode.make(encrypted_product_id)
                img.save("{}.png".format(pid))
        else:
            print('error')
    context = {
        'form': form,
    }
    return render(request,'addProduct', context)














