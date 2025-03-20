var a = 0;
function pass(fieldId) {
  var passwordField = document.getElementById(fieldId);
  var icon = document.getElementById('pass-icon' + (fieldId === 'password' ? '1' : '2'));

  if (a === 1) {
    passwordField.type = 'password';
    icon.classList.remove('fa-eye')
    icon.classList.add('fa-eye-slash');
    a = 0;
  }

  else {
    passwordField.type = 'text';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
    a = 1;
  }
}