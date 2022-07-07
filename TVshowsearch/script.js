const formid = document.querySelector('#formclass');
formid.addEventListener('submit', async function (e) {
    e.preventDefault();
    queryele = document.querySelector("#query");
    query = formid.elements.query.value;
    const res = await axios.get(`https://api.tvmaze.com/search/shows?q=${query}`);
    addshows(res.data);
})
const pdiv = document.querySelector("#qans");
const addshows = (shows) => {
    for (let id of shows) {
        let genre = ""
        console.log(id.show.genres);
        for (let gen of id.show.genres) {
            genre += gen
        }
        const cardhtml = card(id.show.name, id.show.image.medium, genre, id.show.premiered, id.show.summary);
        const ans = document.createElement("DIV");
        ans.innerHTML = cardhtml;
        ans.class = "column";
        pdiv.append(ans);
    }
}
const card = (name, img, genres, release, summary) => {
    console.log(name, img, genres, release, summary)
    return `<div class="card">
  <div class="card-image">
    <figure class="image is-4by3">
      <img src="${img}" alt="Placeholder image">
    </figure>
  </div>
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img src="${img}" alt="Placeholder image">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">${name}</p>
        <p class="subtitle is-6">${release}</p>
        ${genres}
      </div>
    </div>

    <div class="content">
      ${summary}
      <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
    </div>
  </div>
</div>`
}
