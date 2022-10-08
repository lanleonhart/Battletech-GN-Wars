(window.webpackJsonp=window.webpackJsonp||[]).push([[75],{163:function(e,t,a){"use strict";a.r(t),a.d(t,"frontMatter",(function(){return r})),a.d(t,"rightToc",(function(){return o})),a.d(t,"metadata",(function(){return s})),a.d(t,"default",(function(){return u}));var n=a(1),l=a(6),i=(a(0),a(178)),r={id:"release-0.2.0",title:"Release v0.2.0",author:"Richard 'CWolf' Griffiths",author_title:"Developer",author_url:"https://github.com/cwolfs",author_image_url:"https://avatars0.githubusercontent.com/u/7622361",tags:["changelog","release","v0.2.0"]},o=[{value:"Major Features",id:"major-features",children:[]},{value:"Minor Features",id:"minor-features",children:[]},{value:"Changes",id:"changes",children:[]},{value:"Bugs Fixed",id:"bugs-fixed",children:[]}],s={permalink:"/blog/release-0.2.0",source:"@site/blog\\2019-01-13-release-0.2.0.md",description:"This is the full release version of v0.2.0. Like the pre-release it fully supports v1.3 and Flashpoints.",date:"2019-01-13T00:00:00.000Z",tags:[{label:"changelog",permalink:"/blog/tags/changelog"},{label:"release",permalink:"/blog/tags/release"},{label:"v0.2.0",permalink:"/blog/tags/v-0-2-0"}],title:"Release v0.2.0",prevItem:{title:"Release v0.2.1",permalink:"/blog/release-0.2.1"},nextItem:{title:"Release v0.1.0",permalink:"/blog/release-0.1.0"}},c={rightToc:o,metadata:s},d="wrapper";function u(e){var t=e.components,a=Object(l.a)(e,["components"]);return Object(i.b)(d,Object(n.a)({},c,a,{components:t,mdxType:"MDXLayout"}),Object(i.b)("p",null,"This is the full release version of v0.2.0. Like the pre-release it fully supports v1.3 and Flashpoints."),Object(i.b)("h2",{id:"major-features"},"Major Features"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Extended Lances - Increase the size of a faction's lances allowing for clan stars (5 mechs) and reinforced lances / comstar demi-lances (6 mechs). Works for vanilla spawns and Mission Control spawns."),Object(i.b)("li",{parentName:"ul"},"Additional Lances Faction Rep - Allow faction reputation range to select which lance to use"),Object(i.b)("li",{parentName:"ul"},"Additional Lances Elite Lances - Allow elite lances to be selected if allied or enemy with a faction"),Object(i.b)("li",{parentName:"ul"},"Flashpoint options - Allow for disabling Mission Control entirely, or just disabling only Additional Lances for FPs"),Object(i.b)("li",{parentName:"ul"},"Additional Lances Skull Lance Difficulty - Added a full initial set of lances to fit different difficulty levels"),Object(i.b)("li",{parentName:"ul"},"Ally Lance Combat Dialogue - Added more dialogue than the sample amount in v0.2.0a"),Object(i.b)("li",{parentName:"ul"},"Additional Lances Tonnage Restrictions - Ability to disable Additional Lances on various tonnage rules"),Object(i.b)("li",{parentName:"ul"},"BT v1.3 / FP Support"),Object(i.b)("li",{parentName:"ul"},"Ally Lance Combat Dialogue - Unique dialogue per contract type and MC contract type variations if you have an ally lance dropping with you."),Object(i.b)("li",{parentName:"ul"},"Additional Lances Skull Lance Difficulty - Additional Lances now take into account skull difficulty when selecting lances to drop into a contract."),Object(i.b)("li",{parentName:"ul"},"Additional Lances in Battle are Primary Objectives - This makes a lot of sense for a Battle as the contract sometimes would end seemingly at random when the original targets were destroyed."),Object(i.b)("li",{parentName:"ul"},"Hot Drop Safety Features - When dropping into close proximity of enemies hot drop safety features will take effect. In the ",Object(i.b)("inlineCode",{parentName:"li"},"settings.json")," you can modify these. It supports auto-guard, auto-evasion and an option to include the enemies in this protection mode too.")),Object(i.b)("h2",{id:"minor-features"},"Minor Features"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Added damaged lances to the Additional Lances selection"),Object(i.b)("li",{parentName:"ul"},"Added more pilot names for combat dialogue"),Object(i.b)("li",{parentName:"ul"},"Added more pilot portraits for combat dialogue"),Object(i.b)("li",{parentName:"ul"},"Added option to turn ally drop combat dialogue off")),Object(i.b)("h2",{id:"changes"},"Changes"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Changed the Additional Lance keys from all uppercase to upper snake case."),Object(i.b)("li",{parentName:"ul"},"Tweaked the path finder checks for spawning to make it slightly more lenient on sloped spawns")),Object(i.b)("h2",{id:"bugs-fixed"},"Bugs Fixed"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Skirmish would crash if ally combat dialogue referenced 'Commander' string replacement as no Commander exists like in the Sim Game"),Object(i.b)("li",{parentName:"ul"},"Contract Loading Freezes - A few contract loading freezes were fixed"),Object(i.b)("li",{parentName:"ul"},"Contract Loading Loops - A few contract loading loop issues were fixed"),Object(i.b)("li",{parentName:"ul"},"Contract Loading Times Improved - Contract loading times are drastically improved"),Object(i.b)("li",{parentName:"ul"},"Random Spawns Fallback Fixes - Fallbacks weren't always activated correctly and when they were used sometimes the lance orientation was incorrect.")))}u.isMDXComponent=!0},178:function(e,t,a){"use strict";a.d(t,"a",(function(){return o})),a.d(t,"b",(function(){return u}));var n=a(0),l=a.n(n),i=l.a.createContext({}),r=function(e){var t=l.a.useContext(i),a=t;return e&&(a="function"==typeof e?e(t):Object.assign({},t,e)),a},o=function(e){var t=r(e.components);return l.a.createElement(i.Provider,{value:t},e.children)};var s="mdxType",c={inlineCode:"code",wrapper:function(e){var t=e.children;return l.a.createElement(l.a.Fragment,{},t)}},d=Object(n.forwardRef)((function(e,t){var a=e.components,n=e.mdxType,i=e.originalType,o=e.parentName,s=function(e,t){var a={};for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&-1===t.indexOf(n)&&(a[n]=e[n]);return a}(e,["components","mdxType","originalType","parentName"]),d=r(a),u=n,p=d[o+"."+u]||d[u]||c[u]||i;return a?l.a.createElement(p,Object.assign({},{ref:t},s,{components:a})):l.a.createElement(p,Object.assign({},{ref:t},s))}));function u(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=a.length,r=new Array(i);r[0]=d;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o[s]="string"==typeof e?e:n,r[1]=o;for(var u=2;u<i;u++)r[u]=a[u];return l.a.createElement.apply(null,r)}return l.a.createElement.apply(null,a)}d.displayName="MDXCreateElement"}}]);