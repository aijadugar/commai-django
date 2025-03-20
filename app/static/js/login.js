var a=0;
    function pass(){
      var passwordField=document.getElementById('password');
      var icon=document.getElementById('pass-icon');

      if(a===1){
        passwordField.type='password';
        icon.classList.remove('fa-eye')
        icon.classList.add('fa-eye-slash');
        a=0;
      }
  
      else{
        passwordField.type='text';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
        a=1;
      }
    }