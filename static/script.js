// CREATE A FAVORITE BY CLICKING HEART BUTTON
// this works when it is copied and pasted in the console dev tools
 $('.favorite-button').on('click', () => {
        console.log('button clicked!');
        // add the favorite to the database
        // call create_favorite function from crud.py --->
        // favorite = Favorite(user= user, park = park)
            //db.session.add(favorite)
            //db.session.commit()
        //return favorite

        // after park is added to the favorites table, I want 
        // it to disappear off of the search-results page once added
    })


function addFavorite() {
    //call crud function create_favorite here somehow
    
};

$('.favorite-button').on('click', addFavorite);
