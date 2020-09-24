$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (films) {
    $.each(films.results, function (d, pel) {
	  $('#list_movies').append('<li>' + pel.title + '</li>');
	}); 
},'json');
