jQuery(document).ready(function ($) {
  /*! modernizr 3.6.0 (Custom Build) | MIT *
 * https://modernizr.com/download/?-inputtypes-setclasses !
Modernizr.inputtypes.color
Modernizr.inputtypes.date
Modernizr.inputtypes.datetime
Modernizr.inputtypes['datetime-local']
Modernizr.inputtypes.email
Modernizr.inputtypes.month
Modernizr.inputtypes.number
Modernizr.inputtypes.range
Modernizr.inputtypes.search
Modernizr.inputtypes.tel
Modernizr.inputtypes.time
Modernizr.inputtypes.url
Modernizr.inputtypes.week
 */
  !(function (e, t, n) {
    function a(e) {
      var t = u.className,
        n = Modernizr._config.classPrefix || "";
      if ((f && (t = t.baseVal), Modernizr._config.enableJSClass)) {
        var a = new RegExp("(^|\\s)" + n + "no-js(\\s|$)");
        t = t.replace(a, "$1" + n + "js$2");
      }
      Modernizr._config.enableClasses &&
        ((t += " " + n + e.join(" " + n)),
        f ? (u.className.baseVal = t) : (u.className = t));
    }
    function s(e, t) {
      return typeof e === t;
    }
    function i() {
      var e, t, n, a, i, o, c;
      for (var u in r)
        if (r.hasOwnProperty(u)) {
          if (
            ((e = []),
            (t = r[u]),
            t.name &&
              (e.push(t.name.toLowerCase()),
              t.options && t.options.aliases && t.options.aliases.length))
          )
            for (n = 0; n < t.options.aliases.length; n++)
              e.push(t.options.aliases[n].toLowerCase());
          for (
            a = s(t.fn, "function") ? t.fn() : t.fn, i = 0;
            i < e.length;
            i++
          )
            (o = e[i]),
              (c = o.split(".")),
              1 === c.length
                ? (Modernizr[c[0]] = a)
                : (!Modernizr[c[0]] ||
                    Modernizr[c[0]] instanceof Boolean ||
                    (Modernizr[c[0]] = new Boolean(Modernizr[c[0]])),
                  (Modernizr[c[0]][c[1]] = a)),
              l.push((a ? "" : "no-") + c.join("-"));
        }
    }
    function o() {
      return "function" != typeof t.createElement
        ? t.createElement(arguments[0])
        : f
        ? t.createElementNS.call(t, "http://www.w3.org/2000/svg", arguments[0])
        : t.createElement.apply(t, arguments);
    }
    var l = [],
      r = [],
      c = {
        _version: "3.6.0",
        _config: {
          classPrefix: "",
          enableClasses: !0,
          enableJSClass: !0,
          usePrefixes: !0,
        },
        _q: [],
        on: function (e, t) {
          var n = this;
          setTimeout(function () {
            t(n[e]);
          }, 0);
        },
        addTest: function (e, t, n) {
          r.push({ name: e, fn: t, options: n });
        },
        addAsyncTest: function (e) {
          r.push({ name: null, fn: e });
        },
      },
      Modernizr = function () {};
    (Modernizr.prototype = c), (Modernizr = new Modernizr());
    var u = t.documentElement,
      f = "svg" === u.nodeName.toLowerCase(),
      p = o("input"),
      d =
        "search tel url email datetime date month week time datetime-local number range color".split(
          " "
        ),
      m = {};
    (Modernizr.inputtypes = (function (e) {
      for (var a, s, i, o = e.length, l = "1)", r = 0; o > r; r++)
        p.setAttribute("type", (a = e[r])),
          (i = "text" !== p.type && "style" in p),
          i &&
            ((p.value = l),
            (p.style.cssText = "position:absolute;visibility:hidden;"),
            /^range$/.test(a) && p.style.WebkitAppearance !== n
              ? (u.appendChild(p),
                (s = t.defaultView),
                (i =
                  s.getComputedStyle &&
                  "textfield" !==
                    s.getComputedStyle(p, null).WebkitAppearance &&
                  0 !== p.offsetHeight),
                u.removeChild(p))
              : /^(search|tel)$/.test(a) ||
                (i = /^(url|email)$/.test(a)
                  ? p.checkValidity && p.checkValidity() === !1
                  : p.value != l)),
          (m[e[r]] = !!i);
      return m;
    })(d)),
      i(),
      a(l),
      delete c.addTest,
      delete c.addAsyncTest;
    for (var h = 0; h < Modernizr._q.length; h++) Modernizr._q[h]();
    e.Modernizr = Modernizr;
  })(window, document);

  if (!Modernizr.inputtypes.date) {
    $("#error_inputtypes_date_js").css({ display: "" });

    $("input[type=date]").each(function () {
      var val = $(this).attr("value");
      var nam = $(this).attr("name");
      $(this)
        .after(
          $("<textarea></textarea>")
            .attr("name", nam)
            .attr("value", val)
            .css("height", "15px")
            .css("width", "150px")
            .mask("9999-99-99")
        )
        .remove();
    });
  }

  var red = "#FFD6D6";
  var grine = "#A8FFBE";

  $("select").bind("change", f_none_to_js);
  $("select").bind("keyup", f_none_to_js);

  $("textarea").bind("change", f_none_to_js);
  $("textarea").bind("keyup", f_none_to_js);
  $("textarea").bind("keyup", f_count_to_textarea_js);
  $("textarea").bind("change", f_count_to_textarea_js);

  $("input").bind("change", f_none_to_js);
  $("input").bind("keyup", f_none_to_js);

  $("input").bind("keyup", f_count_to_textarea_js);
  $("input").bind("change", f_count_to_textarea_js);

  //устанавливаем фон элемента
  function f_none_to_js() {
    var required = $(this).attr("required");
    //если обязательное для заполнения

    if (required) {
      var v = $(this).val();
      if (v != false || v == "0") return $(this).css({ background: grine });
      return $(this).css({ background: red });
    }
  }

  //пишем после элемента, сколько осталось символов для внесения
  function f_count_to_textarea_js() {
    var maxlength = $(this).attr("maxlength");

    //Если параметр maxlength есть
    if (maxlength) {
      var length = $(this).val().length;

      var itog = maxlength - length;
      //alert (maxlength+' => '+length+' осталось символов => '+itog);
      $(this).next().remove();
      if (itog > 3)
        $(this).after('<span class="grine_bold_text">' + itog + "</span>");
      else $(this).after('<span class="red_bold_text">' + itog + "</span>");
    }
  }

  $("textarea").keyup();
  $("select").keyup();
  $("input").keyup();

  jQuery(window).bind("beforeunload", function (e) {
    var message =
      "Если вы внесли какие либо данные, при переходе с этой страницы они будут потеряны.";
    e.returnValue = message;
    return message;
  });
});
