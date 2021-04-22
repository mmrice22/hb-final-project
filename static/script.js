// CREATE A FAVORITE BY CLICKING HEART BUTTON

const disableFaveButton = () => {
    if ($(".favorite-button").hasClass("clicked")){
        $(".favorite-button").attr('disabled', true)
    };
};


$('.favorite-button').on('click', (evt) => {
    $('.favorite-button').addClass("clicked")
    console.log("button clicked!")
    const clickedBtn = evt.target;
    if (clickedBtn === evt.target){
        disableFaveButton(clickedBtn)
    };
    
});
