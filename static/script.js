// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($("button").hasClass("clicked")){
        $("button.clicked").attr('disabled', true)
    } else {
        $("button").attr('disabled', false)
    };
    
};


$('.favorite-button').on('click', (evt) => {
    $(evt.target).addClass("clicked");
    disableFaveButton(evt.target);
});



