function validate()
{
var username=document.getElementById("username").value;
var password=document.getElementById("password").value;
if(username=="admin"&& password=="user")
{	
	form.submit();
	return true
}
else
{
    alert("login failed");
	return false
	
}


}