(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[1641],{51641:(e,r,t)=>{"use strict";t.r(r);t.d(r,{main:()=>Y});var o=t(85363);var n=t(94278);var l=t(4691);var s=t(36954);var a=t(85745);var i=t(74114);var c=t(28180);var u=t(65053);var f=t(67376);var p=t(38710);var h=t(81554);var d=t(46174);var y=t(66657);var v=t(71821);var b=t(14671);var x=t(69614);var m=t(34802);var j=t(14237);var g=t(54244);var w=t(56329);var C=t(32633);var P=t(72738);var E=t(85357);var S=t(83344);var _=t(11706);var k=t(71e3);var O=t(55337);var L=t(34577);var J=t(95528);var A=t(3268);var N=t(42956);var T=t(50168);var M=t(31105);var $=t(46383);var B=t(71334);var D=t(65540);var R=t(1733);var F=t(67219);var I=t(7560);if(Promise.allSettled===undefined){Promise.allSettled=e=>Promise.all(e.map((e=>e.then((e=>({status:"fulfilled",value:e})),(e=>({status:"rejected",reason:e}))))))}async function U(e,r){try{const t=await window._JUPYTERLAB[e].get(r);return t()}catch(t){console.warn(`Failed to create module: package: ${e}; module: ${r}`);throw t}}async function Y(){var e=o.PageConfig.getOption("browserTest");if(e.toLowerCase()==="true"){var r=document.createElement("div");r.id="browserTest";document.body.appendChild(r);r.textContent="[]";r.style.display="none";var n=[];var l=false;var s=25e3;var a=function(){if(l){return}l=true;r.className="completed"};window.onerror=function(e,t,o,l,s){n.push(String(s));r.textContent=JSON.stringify(n)};console.error=function(e){n.push(String(e));r.textContent=JSON.stringify(n)}}var i=t(27194).JupyterLab;var c=[];var u=[];var f=[];var p=[];const h=[];const d=[];const y=[];const v=JSON.parse(o.PageConfig.getOption("federated_extensions"));const b=[];v.forEach((e=>{if(e.extension){b.push(e.name);h.push(U(e.name,e.extension))}if(e.mimeExtension){b.push(e.name);d.push(U(e.name,e.mimeExtension))}if(e.style){y.push(U(e.name,e.style))}}));function*x(e){let r;if(e.hasOwnProperty("__esModule")){r=e.default}else{r=e}let t=Array.isArray(r)?r:[r];for(let n of t){if(o.PageConfig.Extension.isDisabled(n.id)){c.push(n.id);continue}if(o.PageConfig.Extension.isDeferred(n.id)){u.push(n.id);f.push(n.id)}yield n}}const m=[];if(!b.includes("@jupyterlab/javascript-extension")){try{let e=t(81302);for(let r of x(e)){m.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/json-extension")){try{let e=t(90032);for(let r of x(e)){m.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/pdf-extension")){try{let e=t(53444);for(let r of x(e)){m.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/vega5-extension")){try{let e=t(7573);for(let r of x(e)){m.push(r)}}catch(E){console.error(E)}}const j=await Promise.allSettled(d);j.forEach((e=>{if(e.status==="fulfilled"){for(let r of x(e.value)){m.push(r)}}else{console.error(e.reason)}}));if(!b.includes("@jupyterlab/application-extension")){try{let e=t(19425);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/apputils-extension")){try{let e=t(35839);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/celltags-extension")){try{let e=t(69354);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/codemirror-extension")){try{let e=t(78310);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/completer-extension")){try{let e=t(10775);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/console-extension")){try{let e=t(4853);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/csvviewer-extension")){try{let e=t(98131);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/debugger-extension")){try{let e=t(91825);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/docmanager-extension")){try{let e=t(96225);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/documentsearch-extension")){try{let e=t(21935);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/extensionmanager-extension")){try{let e=t(91390);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/filebrowser-extension")){try{let e=t(46604);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/fileeditor-extension")){try{let e=t(15174);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/help-extension")){try{let e=t(7995);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/htmlviewer-extension")){try{let e=t(65336);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/hub-extension")){try{let e=t(93651);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/imageviewer-extension")){try{let e=t(76660);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/inspector-extension")){try{let e=t(75583);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/launcher-extension")){try{let e=t(44375);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/logconsole-extension")){try{let e=t(43633);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/mainmenu-extension")){try{let e=t(1005);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/markdownviewer-extension")){try{let e=t(38616);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/mathjax2-extension")){try{let e=t(80822);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/notebook-extension")){try{let e=t(38291);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/rendermime-extension")){try{let e=t(70041);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/running-extension")){try{let e=t(60782);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/settingeditor-extension")){try{let e=t(975);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/shortcuts-extension")){try{let e=t(7023);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/statusbar-extension")){try{let e=t(10950);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/terminal-extension")){try{let e=t(78287);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/theme-dark-extension")){try{let e=t(55436);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/theme-light-extension")){try{let e=t(14784);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/toc-extension")){try{let e=t(47011);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/tooltip-extension")){try{let e=t(65804);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/translation-extension")){try{let e=t(956);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/ui-components-extension")){try{let e=t(48833);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}if(!b.includes("@jupyterlab/vdom-extension")){try{let e=t(39388);for(let r of x(e)){p.push(r)}}catch(E){console.error(E)}}const g=await Promise.allSettled(h);g.forEach((e=>{if(e.status==="fulfilled"){for(let r of x(e.value)){p.push(r)}}else{console.error(e.reason)}}));(await Promise.allSettled(y)).filter((({status:e})=>e==="rejected")).forEach((({reason:e})=>{console.error(e)}));const w=new i({mimeExtensions:m,disabled:{matches:c,patterns:o.PageConfig.Extension.disabled.map((function(e){return e.raw}))},deferred:{matches:u,patterns:o.PageConfig.Extension.deferred.map((function(e){return e.raw}))}});p.forEach((function(e){w.registerPluginModule(e)}));w.start({ignorePlugins:f});var C=(o.PageConfig.getOption("exposeAppInBrowser")||"").toLowerCase()==="true";var P=(o.PageConfig.getOption("devMode")||"").toLowerCase()==="true";if(C||P){window.jupyterlab=w}if(e.toLowerCase()==="true"){w.restored.then((function(){a(n)})).catch((function(e){a([`RestoreError: ${e.message}`])}));window.setTimeout((function(){a(n)}),s)}}}}]);