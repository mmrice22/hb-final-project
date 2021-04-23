// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($("button").hasClass("clicked")){
        $("button.clicked").attr('disabled', true)
    };  
};


$('.favorite-button').on('click', (evt) => {
    $(evt.target).addClass("clicked");
    // get info from the div that this button was inside of
    const divData = {
        parkId: $('.park-id').data(),
        // get info stored in element with the class park-name
        parkName: $('.park-name').data(),
        // get info stored in element with the class park-description
        parkDescription: $('.park-description').data(),
        // get info stored in element with the class park-directions
        parkDirections: $('.park-directions').data(),
        // get info stored in element with the class state-code
        parkStateCode: $('.state-code').data()
    };
    console.log(divData);
    // get park data from the route it is in whish is the parks/search
    $.get('/favorites', divData, (res) => {
    //display response from the server
        alert(`This is the response -> ${res}`);

});
    disableFaveButton(evt.target);
});






