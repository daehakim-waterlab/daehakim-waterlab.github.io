// Full-text search box on the Blog page (_pages/blog.md). The index (assets/json/blog-search.json)
// is fetched the first time someone types. A post matches when every word of the query appears
// in its title, description, tags or text (English or the Korean summary); titles and tags rank
// first. While a query is active, the paginated list is hidden and the matches are shown instead.
// The query is kept in the address as ?q=... so a search can be shared or reloaded.
(function () {
  var input = document.getElementById("blog-search-input");
  if (!input) return;
  var box = document.getElementById("blog-search-results");
  var hidden = [document.querySelector(".post-list"), document.querySelector('nav[aria-label="Blog page navigation"]')].filter(Boolean);
  var index = null;
  var loading = null;
  var timer = null;

  function load() {
    if (!loading) {
      loading = fetch(input.getAttribute("data-index"))
        .then(function (r) {
          return r.json();
        })
        .then(function (data) {
          index = data.map(function (p) {
            p._title = p.title.toLowerCase();
            p._meta = (p.tags + " " + p.categories + " " + p.description).toLowerCase();
            p._text = p.text.toLowerCase();
            return p;
          });
        });
    }
    return loading;
  }

  function esc(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function mark(s, terms) {
    var out = esc(s);
    terms.forEach(function (t) {
      var re = new RegExp("(" + esc(t).replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return out;
  }

  function snippet(p, terms) {
    var at = -1;
    for (var i = 0; i < terms.length && at < 0; i++) at = p._text.indexOf(terms[i]);
    if (at < 0) return p.description || "";
    var start = Math.max(0, at - 70);
    var end = Math.min(p.text.length, at + 150);
    // Start and end on whole words.
    if (start > 0) {
      var sp = p.text.indexOf(" ", start);
      if (sp >= 0 && sp < at) start = sp + 1;
    }
    if (end < p.text.length) {
      var ep = p.text.lastIndexOf(" ", end);
      if (ep > at) end = ep;
    }
    return (start > 0 ? "… " : "") + p.text.slice(start, end).trim() + (end < p.text.length ? " …" : "");
  }

  function count(hay, t) {
    var n = 0,
      i = hay.indexOf(t);
    while (i >= 0 && n < 20) {
      n++;
      i = hay.indexOf(t, i + t.length);
    }
    return n;
  }

  function show(on) {
    hidden.forEach(function (el) {
      el.style.display = on ? "none" : "";
    });
    box.hidden = !on;
  }

  function run() {
    var q = input.value.trim();
    var url = new URL(window.location.href);
    if (q) url.searchParams.set("q", q);
    else url.searchParams.delete("q");
    window.history.replaceState(null, "", url);
    if (q.length < 2) {
      show(false);
      box.innerHTML = "";
      return;
    }
    load().then(function () {
      if (input.value.trim() !== q) return;
      var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
      var hits = [];
      index.forEach(function (p) {
        var score = 0;
        for (var i = 0; i < terms.length; i++) {
          var t = terms[i];
          var inTitle = p._title.indexOf(t) >= 0;
          var inMeta = p._meta.indexOf(t) >= 0;
          var inText = count(p._text, t);
          if (!inTitle && !inMeta && !inText) return;
          score += (inTitle ? 20 : 0) + (inMeta ? 8 : 0) + inText;
        }
        hits.push({ p: p, score: score });
      });
      hits.sort(function (a, b) {
        return b.score - a.score;
      });
      var html =
        '<p class="blog-search-count">' +
        (hits.length ? hits.length + (hits.length === 1 ? " post matches " : " posts match ") : "No posts match ") +
        "“" +
        esc(q) +
        "”.</p>";
      if (hits.length) {
        html +=
          '<ul class="post-list">' +
          hits
            .map(function (h) {
              var p = h.p;
              return (
                '<li><h3><a class="post-title" href="' +
                p.url +
                '">' +
                mark(p.title, terms) +
                '</a></h3><p class="blog-search-snippet">' +
                mark(snippet(p, terms), terms) +
                '</p><p class="post-meta">' +
                esc(p.date) +
                "</p></li>"
              );
            })
            .join("") +
          "</ul>";
      }
      box.innerHTML = html;
      show(true);
    });
  }

  input.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(run, 150);
  });
  input.addEventListener("focus", load, { once: true });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      input.value = "";
      run();
    }
  });
  var q0 = new URL(window.location.href).searchParams.get("q");
  if (q0) {
    input.value = q0;
    run();
  }
})();
