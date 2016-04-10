function validateForm(){
    x = document.forms["loginForm"]["username"].value;
    if( x == null || x == "" ){
        console.log("asd");
        alert("Login must be filled");
        return false;
    }
}
