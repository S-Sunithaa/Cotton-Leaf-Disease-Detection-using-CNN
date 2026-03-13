from django.shortcuts import render , redirect, get_object_or_404
from user.models import UserReg
from user.forms import Register_Form
from django.contrib import messages
from admins.models import image_uoload
# Create your views here.

def userhome(request):
  return render(request, 'users/UserHomePage.html')

def UserRegister(request):
  
  forms = Register_Form()
  
  if request.method =='POST':
    form = Register_Form(request.POST , request.FILES)
    print(form)
    
    if form.is_valid():
       form.save()
       print('Data Saved Sucessfully---')
       return redirect('userlogin')
    else:
       print('data not saved--')
  return render(request , 'UserRegistrations.html' , {'forms' :forms})     

def userlogin(request):
  
  if request.method=='POST':
    
    username=request.POST.get('loginid')
    password = request.POST.get('pswd')
    
    try:
      
      check=UserReg.objects.get(username=username, password=password)
      status=check.status
      
      if status == 'Activated' or status == 'activated':
        request.session['id']=check.id
       # request.session['name']=check.name
        request.session['username'] =username
        request.session['mobile_no'] =check.mobile_no
        request.session['email'] =check.email
        return render(request , 'users/UserHomePage.html' )
      else:
        print('login error')
        
    except Exception as e:
       print('Exception as', str(e))
       a =  "User is not authorised by admin "
       return render(request, 'UserLogin.html' , {'a':a})
     
  return render(request, 'UserLogin.html')
  
 

def Predication(request):
    saved_image=None
    result =None
    from user.utility.predication import predict
    if request.method == "POST":
        imag = request.FILES.get('path1')
        print(imag)
        
        if imag:
            # Save the uploaded image
            image_instance = image_uoload.objects.create(image=imag)
            print('Image saved successfully')
            
            # Retrieve the saved image by ID
            image_id = image_instance.id
            saved_image = get_object_or_404(image_uoload, pk=image_id)
            print('Final path is:', saved_image)
            saved_image=saved_image
            # Perform prediction
            result = predict(saved_image.image.path)  # Pass the file path to the predict function
            print('Prediction is', result)
            result=result
            image_uoload.objects.get(pk=image_id).delete()
        else:
            print('Image path is empty ')
    context={
      'saved_images' :saved_image,
       'result' :result
    }
    return render(request, 'users/Predication.html' , context)
  
  
  
