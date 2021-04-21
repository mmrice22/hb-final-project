// CREATE A FAVORITE BY CLICKING HEART BUTTON
// this works when it is copied and pasted in the console dev tools
 $('.favorite-button').on('click', () => {
        //alert('button clicked!');
        console.log('button clicked')
        // add the favorite to the database
        // call create_favorite function from crud.py --->
        // favorite = Favorite(user= user, park = park)
            //db.session.add(favorite)
            //db.session.commit()
        //return favorite

        // after park is added to the favorites table, I want 
        // it to disappear off of the search-results page once added
    })


//let addFavorite = (park) => {
    //call crud function create_favorite here somehow
  //  $('.favorited-park').append(`${park}`);
    //alert('button clicked!');
    //console.log(park);

    
    //$(`.favorited-park`).html(park);
//};

//$('.favorite-button').on('click', addFavorite);


const disableFaveButton = (buttonEl) => {
    $(buttonEl).attr('disabled', true);
};


$('.favorite-button').on('click', (evt) => {
    evt.preventDefault();
    const clickedBtn = evt.target;
    disableFaveButton(clickedBtn)
});
