function togglePublicationPanel(control) {
  const links = control.closest(".links");
  const entry = links?.parentElement;
  if (!entry) return;

  const panelType = ["abstract", "award", "bibtex"].find((type) => control.classList.contains(type));
  if (!panelType) return;

  const targetPanels = entry.querySelectorAll(`.${panelType}.hidden`);
  const shouldOpen = Array.from(targetPanels).some((panel) => !panel.classList.contains("open"));

  entry.querySelectorAll(".abstract.hidden, .award.hidden, .bibtex.hidden").forEach((panel) => {
    panel.classList.toggle("open", shouldOpen && panel.classList.contains(panelType));
  });
}

function toggleMoreAuthors(control) {
  const isExpanded = control.getAttribute("aria-expanded") === "true";
  control.innerHTML = isExpanded ? control.dataset.collapsedText : control.dataset.expandedHtml;
  control.setAttribute("aria-expanded", String(!isExpanded));
  control.removeAttribute("title");
}

document.addEventListener("click", (event) => {
  const publicationControl = event.target.closest("a.abstract, a.award, a.bibtex");
  if (publicationControl) {
    event.preventDefault();
    togglePublicationPanel(publicationControl);
    return;
  }

  const moreAuthorsControl = event.target.closest(".more-authors");
  if (moreAuthorsControl) toggleMoreAuthors(moreAuthorsControl);
});

document.addEventListener("keydown", (event) => {
  if ((event.key === "Enter" || event.key === " ") && event.target.matches(".more-authors")) {
    event.preventDefault();
    toggleMoreAuthors(event.target);
  }
});

if (typeof window.jQuery !== "undefined") {
  $(document).ready(function () {
    $("a").removeClass("waves-effect waves-light");

    // bootstrap-toc
    if ($("#toc-sidebar").length) {
      // remove related publications years from the TOC
      $(".publications h2").each(function () {
        $(this).attr("data-toc-skip", "");
      });
      var navSelector = "#toc-sidebar";
      var $myNav = $(navSelector);
      Toc.init($myNav);
      $("body").scrollspy({
        target: navSelector,
      });
    }

    // add css to jupyter notebooks
    const cssLink = document.createElement("link");
    cssLink.href = "../css/jupyter.css";
    cssLink.rel = "stylesheet";
    cssLink.type = "text/css";

    let jupyterTheme = determineComputedTheme();

    $(".jupyter-notebook-iframe-container iframe").each(function () {
      $(this).contents().find("head").append(cssLink);

      if (jupyterTheme == "dark") {
        $(this).bind("load", function () {
          $(this).contents().find("body").attr({
            "data-jp-theme-light": "false",
            "data-jp-theme-name": "JupyterLab Dark",
          });
        });
      }
    });

    // trigger popovers
    $('[data-toggle="popover"]').popover({
      trigger: "hover",
    });
  });
}
