(function () {
  var d = document, header = d.querySelector(".site-header");
  var menuBtn = d.querySelector(".menu-btn"), menu = d.querySelector(".menu");
  var closeBtn = menu.querySelector(".menu-close");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  d.documentElement.classList.add("is-ready");

  function onScroll() { header.classList.toggle("is-scrolled", scrollY > 8); }
  onScroll();
  addEventListener("scroll", onScroll, { passive: true });

  function setOpen(open) {
    menu.hidden = !open;
    menuBtn.setAttribute("aria-expanded", String(open));
    d.body.classList.toggle("menu-open", open);
    (open ? closeBtn : menuBtn).focus();
  }
  menuBtn.onclick = function () { setOpen(menu.hidden); };
  closeBtn.onclick = function () { setOpen(false); };
  menu.onclick = function (e) { if (e.target.closest("a")) setOpen(false); };
  addEventListener("keydown", function (e) {
    if (menu.hidden) return;
    if (e.key === "Escape") return setOpen(false);
    if (e.key !== "Tab") return;
    var q = [].slice.call(menu.querySelectorAll("button, a:not([hidden])"));
    var i = q.indexOf(d.activeElement);
    e.preventDefault();
    q[(i + (e.shiftKey ? -1 : 1) + q.length) % q.length].focus();
  });

  function show(src, sel, flag) {
    var probe = new Image();
    probe.onload = function () {
      d.querySelectorAll(sel).forEach(function (img) {
        img.src = src;
        img.hidden = false;
        var panel = img.closest("[data-panel]");
        if (panel) panel.classList.add(flag);
      });
    };
    probe.src = src;
  }
  var cut = new Image();
  cut.onload = function () { show("assets/img/drashti-cutout.png", ".portrait--cutout", "has-cutout"); };
  cut.onerror = function () { show("assets/img/drashti.jpg", ".portrait--photo", "has-photo"); };
  cut.src = "assets/img/drashti-cutout.png";
  show("assets/img/drashti-2.jpg", ".portrait--second", "has-second");

  var links = [].filter.call(d.querySelectorAll(".nav a[href^='#'], .menu a[href^='#']"), function (a) {
    return !a.closest("[hidden]");
  });
  var seen = {}, sections = [];
  links.forEach(function (a) {
    var id = a.hash.slice(1), section = d.getElementById(id);
    if (!seen[id] && section && !section.hidden) { seen[id] = 1; sections.push(section); }
  });
  function current(id) {
    links.forEach(function (a) {
      if (a.hash === "#" + id) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }
  var active = new Map();
  var watch = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) active.set(entry.target.id, entry.boundingClientRect.top);
      else active.delete(entry.target.id);
    });
    if (scrollY > 80 && innerHeight + scrollY >= d.documentElement.scrollHeight - 8) return current("contact");
    var best = "", top = 1 / 0;
    active.forEach(function (y, id) { if (y < top) { top = y; best = id; } });
    current(best || "hero");
  }, { rootMargin: "-80px 0px -45% 0px", threshold: 0 });
  sections.forEach(function (section) { watch.observe(section); });

  function markIn(el) { el.classList.add("is-in"); }
  if (reduce) {
    d.querySelectorAll(".reveal, .side-panel").forEach(markIn);
  } else {
    var reveal = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        markIn(entry.target);
        reveal.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.1 });
    d.querySelectorAll(".reveal, .side-panel").forEach(function (el) { reveal.observe(el); });
  }

  var pageUrl = location.href.split("#")[0];
  var shareText = "Portfolio of Drashti Baser — law student focused on litigation, legal research, and drafting.";
  var wa = d.getElementById("share-whatsapp");
  var li = d.getElementById("share-linkedin");
  var copyBtn = d.getElementById("copy-link");
  if (wa) wa.href = "https://wa.me/?text=" + encodeURIComponent(shareText + " " + pageUrl);
  if (li) li.href = "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(pageUrl);
  if (copyBtn) {
    copyBtn.onclick = function () {
      var done = function () {
        var label = copyBtn.getAttribute("data-copied") || "Link copied";
        var prev = copyBtn.textContent;
        copyBtn.textContent = label;
        copyBtn.classList.add("is-copied");
        setTimeout(function () {
          copyBtn.textContent = prev;
          copyBtn.classList.remove("is-copied");
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(pageUrl).then(done).catch(function () {
          window.prompt("Copy this link", pageUrl);
        });
      } else {
        window.prompt("Copy this link", pageUrl);
      }
    };
  }

  var newsList = d.getElementById("law-news");
  var newsFallback = d.getElementById("law-news-fallback");
  var newsStatus = d.getElementById("law-desk-status");
  if (newsList && newsFallback && newsStatus) {
    var rssQuery = 'law students OR "legal education" OR CLAT OR "Bar Council" India';
    var rssUrl = "https://news.google.com/rss/search?q=" + encodeURIComponent(rssQuery) +
      "&hl=en-IN&gl=IN&ceid=IN:en";
    var feedApi = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent(rssUrl);

    function splitTitle(raw) {
      var parts = String(raw || "").split(" - ");
      if (parts.length < 2) return { title: raw, source: "News" };
      return { title: parts.slice(0, -1).join(" - ").trim(), source: parts[parts.length - 1].trim() };
    }

    function formatDate(value) {
      var date = new Date(value);
      if (isNaN(date.getTime())) return "";
      return date.toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" });
    }

    function showFallback() {
      newsList.hidden = true;
      newsFallback.hidden = false;
      newsStatus.textContent = "Offline — try the desks below";
    }

    fetch(feedApi)
      .then(function (res) { return res.json(); })
      .then(function (data) {
        if (!data || data.status !== "ok" || !data.items || !data.items.length) {
          return showFallback();
        }
        var seen = {};
        var items = [];
        data.items.forEach(function (item) {
          if (items.length >= 5) return;
          var parsed = splitTitle(item.title);
          var key = parsed.title.toLowerCase().slice(0, 48);
          if (seen[key]) return;
          seen[key] = 1;
          items.push({
            title: parsed.title,
            source: parsed.source,
            link: item.link,
            date: formatDate(item.pubDate)
          });
        });
        if (!items.length) return showFallback();
        newsList.innerHTML = items.map(function (item) {
          return "<li><a href=\"" + item.link + "\" target=\"_blank\" rel=\"noopener noreferrer\">" +
            item.title + " <span class=\"sr-only\">(opens in a new tab)</span></a>" +
            "<div class=\"news-meta\"><span>" + item.source + "</span>" +
            (item.date ? "<span>" + item.date + "</span>" : "") +
            "</div></li>";
        }).join("");
        newsFallback.hidden = true;
        newsList.hidden = false;
        newsStatus.textContent = "Updated just now";
      })
      .catch(showFallback);
  }
})();
