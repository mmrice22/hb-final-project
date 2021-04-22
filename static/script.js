// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($(evt.target).hasClass("clicked")){
        $(".favorite-button").attr('disabled', true)
    };
};


$('.favorite-button').on('click', (evt) => {
    $(evt.target).addClass("clicked")
    console.log("button clicked!")
    const clickedBtn = evt.target;
    if (clickedBtn === evt.target){
        disableFaveButton(clickedBtn)
    };
});



