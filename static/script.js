// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($("button").hasClass("clicked")){
        $("button.clicked").attr('disabled', true)
    };  
};


$('.favorite-button').on('click', (evt) => {
    $(evt.target).addClass("clicked");
    //console.log(evt.target.value)
    // get info from the div that this button was inside of
    const parkCode = evt.target.value
    // get park data from the route it is in whish is the parks/search
    $.get('/makefavorite', {"parkCode": parkCode}, (res) => {
    //display response from the server
        alert(`This is the response -> ${res}`);
        
});
    disableFaveButton(evt.target);
});






