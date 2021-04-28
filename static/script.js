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
    $.get('/makefavorite.json', {"parkCode": parkCode}, (res) => {
    //display response from the server
        alert(`You've successfully added ${res} to your favorites!`);
        
});
    disableFaveButton(evt.target);
});



const disableCheckButton = () => {
    if ($("button").hasClass("clicked")){
        $("button.clicked").attr('disabled', true)
    };  
};


$('.been-button').on('click', (evt) => {
    $(evt.target).addClass("clicked");
    console.log(evt.target);
    const data = {
        'hasBeen': $('.has-been').val()
    };

    $.post('/visited.json', data, (res) => {
        alert(res)
    });
    disableCheckButton(evt.target);
});






