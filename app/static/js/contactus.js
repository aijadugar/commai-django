 // JavaScript for Interactive Validation
 const contactForm = document.getElementById('contactForm');
 const nameInput = document.getElementById('name');
 const emailInput = document.getElementById('email');
 const messageInput = document.getElementById('message');
 const nameError = document.getElementById('nameError');
 const emailError = document.getElementById('emailError');
 const messageError = document.getElementById('messageError');

 contactForm.addEventListener('submit', function(event) {
     let isValid = true;

     // Validate Name
     if (nameInput.value.trim() === '') {
         nameError.textContent = 'Name is required.';
         isValid = false;
     } else {
         nameError.textContent = '';
     }

     // Validate Email
     const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
     if (!emailPattern.test(emailInput.value.trim())) {
         emailError.textContent = 'Enter a valid email address.';
         isValid = false;
     } else {
         emailError.textContent = '';
     }

     // Validate Message
     if (messageInput.value.trim() === '') {
         messageError.textContent = 'Message cannot be empty.';
         isValid = false;
     } else {
         messageError.textContent = '';
     }

     if (!isValid) {
         event.preventDefault();
     }
 });