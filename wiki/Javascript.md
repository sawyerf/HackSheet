<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/206203840-838abafb-ae95-4fbe-a371-2a47873f06ea.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/22857002/206203842-e69da53d-2978-407c-abc7-1c463e988f09.svg#gh-light-mode-only">
</picture>

---

- [Fetch](#fetch)
- [Open url](#open-url)

# Fetch
### Get
```js
fetch('http://example.com/', {options})
.then(data => {
	console.log(data);
})
.catch(err => {
	console.log(err);
})
```

### Post
```js
fetch("http://example.com/api/example", {
    method: "POST",
    body: JSON.stringify({
        data: "lolipop",
    }),
    headers: {
        "Content-type": "application/json"
    }
})
.then(response => response.json())
.then(json => console.log(json));
```

# Open url
### New tab
```js
window.open('http://example.com');
```

### Change url
```js
document.location = 'http://example.com/''
```