# ☕ Javascript

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