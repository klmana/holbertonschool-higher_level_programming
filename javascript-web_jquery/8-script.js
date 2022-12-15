// JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    $.each(data.results, function (i, item) {
        $('UL#list_movies').append('<li>' + item.title + '</li>');
    });
    });
