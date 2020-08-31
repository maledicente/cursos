const scrapeIt = require("scrape-it")

scrapeIt("https://www.imdb.com/name/nm0000115/",{
	movies: {
		listItem: "[id^=actor-]",
		data: {
			url: {
				selector: 'a:first-child',
				attr: 'href'
			}
		}
	}
})
.then( page => {
	urls = page.movies.map( movie => 'http://www.imdb.com' + movie.url)

Promise.all(urls.map( url => getPage(url) ))
	.then(result => {
		console.log(result);
	})
})
.catch( err => console.log(err));


var getPage = url => {
	console.log( `Starting ${url} `)
	return scrapeIt(url, {
    title: "h1"
  , summary: "div.summary_text"
  , rating: "[itemprop=ratingValue]"
	}).catch( err => console.log(err));
}

// Promise interface
Promise.all([getPage("https://www.imdb.com/title/tt1274586/")])
.then(data => console.log(data))
