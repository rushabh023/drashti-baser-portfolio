(function () {
  var d = document, header = d.querySelector(".site-header");
  var menuBtn = d.querySelector(".menu-btn"), menu = d.querySelector(".menu");
  var closeBtn = menu.querySelector(".menu-close");
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
})();
