(function () {
  var d = document;
  var header = d.querySelector(".site-header");
  var menuBtn = d.querySelector(".menu-btn");
  var menu = d.querySelector(".menu");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  d.documentElement.classList.add("is-ready");

  if (header) {
    function onScroll() { header.classList.toggle("is-scrolled", scrollY > 8); }
    onScroll();
    addEventListener("scroll", onScroll, { passive: true });
  }

  if (menuBtn && menu) {
    var closeBtn = menu.querySelector(".menu-close");
    function setOpen(open) {
      menu.hidden = !open;
      menuBtn.setAttribute("aria-expanded", String(open));
      d.body.classList.toggle("menu-open", open);
      (open ? closeBtn : menuBtn).focus();
    }
    menuBtn.onclick = function () { setOpen(menu.hidden); };
    if (closeBtn) closeBtn.onclick = function () { setOpen(false); };
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
  }

  function markIn(el) { el.classList.add("is-in"); }
  if (reduce) {
    d.querySelectorAll(".reveal").forEach(markIn);
  } else {
    var reveal = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        markIn(entry.target);
        reveal.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.1 });
    d.querySelectorAll(".reveal").forEach(function (el) { reveal.observe(el); });
  }

  var pageUrl = location.href.split("#")[0];
  var shareText = "Student tools from Drashti Baser's law portfolio — playbooks, checklists, and resources for classmates.";
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

  /* Law desk — free APIs */
  var newsList = d.getElementById("law-news");
  var newsFallback = d.getElementById("law-news-fallback");
  var newsStatus = d.getElementById("law-desk-status");
  if (newsList && newsFallback && newsStatus) {
    var FREE_NEWS = "https://freenewsapi.ai/v1/search";
    var fields = "title,url,published_at,sitename,host";

    function escapeHtml(value) {
      return String(value || "")
        .replace(/&/g, "&amp;").replace(/</g, "&lt;")
        .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
    }
    function decodeEntities(value) {
      var box = d.createElement("textarea");
      box.innerHTML = String(value || "");
      return box.value;
    }
    function formatDate(value) {
      var date = new Date(value);
      if (isNaN(date.getTime())) return "";
      return date.toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" });
    }
    function sourceLabel(item) {
      var host = (item.host || "").toLowerCase();
      if (host.indexOf("livelaw") !== -1) return "LiveLaw";
      if (host.indexOf("barandbench") !== -1) return "Bar & Bench";
      var name = decodeEntities(item.sitename || "").replace(/\s+/g, " ").trim();
      if (name && name.length < 40) return name;
      return host || "News";
    }
    function showFallback() {
      newsList.hidden = true;
      newsFallback.hidden = false;
      newsStatus.textContent = "Offline — try the desks below";
    }
    function renderItems(items) {
      if (!items.length) return showFallback();
      newsList.innerHTML = items.map(function (item) {
        return "<li><a href=\"" + escapeHtml(item.link) + "\" target=\"_blank\" rel=\"noopener noreferrer\">" +
          escapeHtml(item.title) + " <span class=\"sr-only\">(opens in a new tab)</span></a>" +
          "<div class=\"news-meta\"><span>" + escapeHtml(item.source) + "</span>" +
          (item.date ? "<span>" + escapeHtml(item.date) + "</span>" : "") +
          "</div></li>";
      }).join("");
      newsFallback.hidden = true;
      newsList.hidden = false;
      newsStatus.textContent = "Live via free APIs";
    }
    function normalizeFreeNews(results) {
      return (results || []).map(function (item) {
        return {
          title: decodeEntities(item.title || "").trim(),
          link: item.url,
          source: sourceLabel(item),
          date: formatDate(item.published_at),
          stamp: new Date(item.published_at).getTime() || 0
        };
      }).filter(function (item) { return item.title && item.link; });
    }
    function dedupeSort(list, limit) {
      var seen = {};
      var out = [];
      list.sort(function (a, b) { return b.stamp - a.stamp; });
      list.forEach(function (item) {
        if (out.length >= limit) return;
        var key = item.title.toLowerCase().slice(0, 52);
        if (seen[key]) return;
        seen[key] = 1;
        out.push(item);
      });
      return out;
    }
    function freeNewsUrl(params) {
      return FREE_NEWS + "?" + params + "&fields=" + encodeURIComponent(fields);
    }
    Promise.all([
      fetch(freeNewsUrl("host=www.livelaw.in&size=4")).then(function (r) { return r.json(); }),
      fetch(freeNewsUrl("host=www.barandbench.com&size=3")).then(function (r) { return r.json(); }),
      fetch(freeNewsUrl("q=" + encodeURIComponent('"law students" OR CLAT OR "legal education" India') + "&size=4"))
        .then(function (r) { return r.json(); })
    ]).then(function (packs) {
      var merged = [];
      packs.forEach(function (pack) {
        if (pack && pack.results && pack.results.length) {
          merged = merged.concat(normalizeFreeNews(pack.results));
        }
      });
      var items = dedupeSort(merged, 6);
      if (!items.length) throw new Error("empty");
      renderItems(items);
    }).catch(showFallback);
  }

  /* Ask / suggest forms → LinkedIn or mailto draft */
  function wireMailtoForm(formId) {
    var form = d.getElementById(formId);
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (value, key) {
        if (String(value).trim()) lines.push(key + ": " + String(value).trim());
      });
      var subject = form.getAttribute("data-subject") || "Message from Students Hub";
      var body = lines.join("\n");
      var mail = form.getAttribute("data-mailto") || "";
      if (mail) {
        location.href = "mailto:" + mail + "?subject=" + encodeURIComponent(subject) +
          "&body=" + encodeURIComponent(body);
      } else {
        var linkedin = form.getAttribute("data-linkedin") || "https://www.linkedin.com/in/drashti-baser";
        try {
          sessionStorage.setItem("students-form-draft", body);
        } catch (err) {}
        window.open(linkedin, "_blank", "noopener,noreferrer");
        alert("LinkedIn will open. Paste your draft from the form into a message. A copy is also in your session if you reopen this page.");
      }
    });
  }
  wireMailtoForm("ask-form");
  wireMailtoForm("suggest-form");

  /* Checklist persistence */
  var checks = d.querySelectorAll(".check-list input[type='checkbox'][data-key]");
  checks.forEach(function (box) {
    var key = "check:" + box.getAttribute("data-key");
    try {
      box.checked = localStorage.getItem(key) === "1";
    } catch (err) {}
    box.addEventListener("change", function () {
      try {
        localStorage.setItem(key, box.checked ? "1" : "0");
      } catch (err2) {}
    });
  });
})();
