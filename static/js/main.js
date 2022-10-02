
const newcust = document.getElementById('userform');
function toggleForm() {
    if (document.getElementById('new').checked){
    newcust.style.visibility = 'visible';
    } else if (document.getElementById('update').checked){
    newcust.style.visibility = 'visible'
    } else {
    newcust.style.visibility = 'hidden'
    }
}
const radioButtons = document.querySelectorAll('input[name="custtype"]');
radioButtons.forEach(radio => {
  radio.addEventListener('click', toggleForm);
});

(function($) {

  $('#reset').on('click', function(){
      $('#userform').reset();
      $('#register-form').reset()
  });
  

  $('#register-form').validate({
    rules : { 
        first_name : {
            required: true,
        },
        last_name : {
            required: true,
        },
        company : {
            required: false
        },
        vin : {
            required: true
        },
        license_plate : {
            required: true
        },
        email : {
            required: true,
            email : true
        },
        phone_number : {
            required: true
            
    },
        
    },

    onfocusout: function(element) {
        $(element).valid();
    },
});

    jQuery.extend(jQuery.validator.messages, {
        required: "",
        remote: "",
        email: "",
        url: "",
        date: "",
        dateISO: "",
        number: "",
        digits: "",
        creditcard: "",
        equalTo: ""
    });
})(jQuery);