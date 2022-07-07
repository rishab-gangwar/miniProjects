const ul = document.querySelector("#jokes");
const addjokes = async () => {
    const joketext = await getdadjokes();
    const li = document.createElement("LI");
    li.append(joketext);
    ul.append(li);
}
const getdadjokes = async () => {
    try {
        const config = {
            headers: {
                Accept: 'application/json'
            }
        }
        const res = await axios.get("https://icanhazdadjoke.com/", config)
        return res.data.joke;
    }
    catch (e) {
        console.log("error in fetching jokes");
    }
}
const button = document.querySelector('button');
button.addEventListener('click', addjokes);