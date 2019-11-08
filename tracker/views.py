from django.shortcuts import render,redirect,render_to_response
from django.conf import settings

from .models import Register,Customer
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):

    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        course=request.POST['course']
        source=request.POST['source']
        leadstatus=request.POST['leadstatus']
        demodate=request.POST['demodate']
        counsler=request.POST['counsler']
        remarks=request.POST['remarks']
        Register.objects.create(name=name,mobile=mobile,email=email,
        course=course,source=source,leadstatus=leadstatus,demodate=demodate,
        counsler=counsler,remarks=remarks)
        # email1=[email]
        # subject ="Registation Conformation"
        # body = "THANKS FOR REGISTRATING IN OUR WEB SITE"
        # send_mail(subject,body,settings.EMAIL_HOST_USER, email1,fail_silently=True)


        messages.success(request,'your registation successful!')

        return redirect('indexpage')
    return render(request,'register.html')

def walkins(request):
    data = Register.objects.all()
    return render_to_response('walkins.html', {'obj':data})
    # return render(request,'walkins.html')


def callings(request):
    if request.method == 'POST':
        leadstatus1 = request.POST['leadstatus']
        # print(leadstatus1)
        demodate1 = request.POST['demodate']
        # print(demodate1)
        obj = Register.objects.filter(leadstatus = leadstatus1).filter(demodate = demodate1)
        return render(request,'call.html', {'obj':obj})
    return render(request,'callings.html')



def counclling(request):
    if request.method == 'POST':
        course = request.POST['course']
        demodate = request.POST['demodate']
        obj = Register.objects.filter(course = course).filter(demodate = demodate)
        return render(request,'counc.html', {'obj':obj})    

    return render(request,'councling.html')
    
def Joinings(request, id):
	joiner = Register.objects.get(id=id)
	if request.method == 'POST':
		name= request.POST['name']
		course= request.POST['course']
		completiondate= request.POST['completiondate']
		datejoining= request.POST['datejoining']
		coursefee= request.POST['coursefee']
		instructor= request.POST['instructor']
		aadhar= request.POST['aadhar']
		mobile= request.POST['mobile']
		email= request.POST['email']
		remark= request.POST['Remarks']
		joiner.name = name
		joiner.course = course
		joiner.mobile = mobile
		joiner.email = email
		joiner.remarks = remark
		joiner.status = "joined"
		joiner.save()
		Customer.objects.create(email=joiner,completiondate=completiondate,datejoining=datejoining,coursefee=coursefee,instructor=instructor,aadhar=aadhar)
		return redirect('studentspage')

	return render(request, 'joinings.html',{'joiner':joiner})

def Joining(request):
	if request.method == 'POST':
		name= request.POST['name']
		course= request.POST['course']
		completiondate= request.POST['completiondate']
		datejoining= request.POST['datejoining']
		coursefee= request.POST['coursefee']
		instructor= request.POST['instructor']
		aadhar= request.POST['aadhar']
		mobile= request.POST['mobile']
		email= request.POST['email']
		remark= request.POST['remark']
		source = request.POST['source']
		Register.objects.create(name=name,mobile=mobile,email=email,course=course, source=source,leadstatus='none', demodate=datejoining, counsler=instructor,remarks=remark,status="joined")
		Customer.objects.create(email=joiner,completiondate=completiondate,datejoining=datejoining,coursefee=coursefee,instructor=instructor,aadhar=aadhar)
		return redirect('studentspage')
	return render(request, 'joining.html')


def Willing(request, id):
	willer = Register.objects.get(id=id)
	if request.method == 'POST':
		willdate = request.POST['demodate']
		willer.demodate = willdate
		willer.save()
		return redirect('walkinspage')

	return render(request, 'willing.html', {'willer':willer})



def Dead(request, id):
	person = Register.objects.get(id=id)
	person.delete()
	return redirect('walkinspage')


def Students(request):
	cstudents = Customer.objects.filter(customerstatus='completed')
	ostudents = Customer.objects.filter(customerstatus='ongoing')
	sstudents = Customer.objects.filter(customerstatus='stopped')
	# sstudents = Customer.objects.filter(customerstatus='stopped').prefetch_related('email')
	# print("{}".format(cstudents[0].email.name))
	return render(request, 'students.html', {'cstudents':cstudents, 'ostudents':ostudents, 'sstudents':sstudents})


def Rejoin(request, id):
	rjstudent = Customer.objects.get(id=id)
	print("{}".format(rjstudent))
	if request.method == 'POST':
		completiondate = request.POST['completiondate']
		rjstudent.completiondate = completiondate
		rjstudent.customerstatus = 'ongoing'
		rjstudent.save()
		return redirect('studentspage')
	return render(request, 'update.html', {'rjstudent':rjstudent})

def Currentstatus(request):
	student = Customer.objects.filter(customerstatus='ongoing')
	return render(request, 'currentstatus.html', {'student':student})

def Complete(request, id):
	student = Customer.objects.get(id=id)
	student.customerstatus = "completed"
	student.save()
	return redirect('studentspage')

def Stopped(request, id):
	student = Customer.objects.get(id=id)
	student.customerstatus = "stopped"
	student.save()
	return redirect('studentspage')