﻿CKEDITOR.dialog.add("videoDialog",function(a){return{title:"Insert a Youtube/Vimeo URL or embed code",minWidth:400,minHeight:100,contents:[{id:"tab-basic",label:"Basic Settings",elements:[{type:"text",id:"url_video",label:"Youtube/Vimeo URL or embed code",validate:CKEDITOR.dialog.validate.notEmpty("Empty!")}]}],onOk:function(){var b=detectar(),c="";"youtube"==b.reproductor?c="https://www.youtube.com/embed/"+b.id_video+"?autohide\x3d1\x26controls\x3d1\x26showinfo\x3d0":
"vimeo"==b.reproductor?c="https://player.vimeo.com/video/"+b.id_video+"?portrait\x3d0";b=new CKEDITOR.dom.element("div");b.setAttribute("class","videodetector");var e=new CKEDITOR.dom.element("iframe");e.setAttribute("src",c);e.setAttribute("frameborder","0");b.append(e);var d=new CKEDITOR.dom.element("input");d.setAttribute("type","button");
b.append(d);a.insertElement(b);d.on("click",function(){d.getParent().remove()})}}});
function detectar(){var a=document.getElementsByClassName("cke_dialog_contents").item(0).getElementsByTagName("input").item(0).value,b="",c="";0<=a.indexOf("youtu.be")&&(c="youtube",b=a.substring(a.lastIndexOf("/")+1,a.length));0<=a.indexOf("youtube")&&(c="youtube",0<=a.indexOf("\x3c/iframe\x3e")?(b=a.substring(a.indexOf("embed/")+6,a.length),b=b.substring(b.indexOf('"'),0)):b=0<=a.indexOf("\x26")?a.substring(a.indexOf("?v\x3d")+3,a.indexOf("\x26")):a.substring(a.indexOf("?v\x3d")+3,a.length));0<=
a.indexOf("vimeo")&&(c="vimeo",0<=a.indexOf("\x3c/iframe\x3e")?(b=a.substring(a.lastIndexOf('vimeo.com/"')+6,a.indexOf("\x3e")),b=b.substring(b.lastIndexOf("/")+1,b.indexOf('"',b.lastIndexOf("/")+1))):b=a.substring(a.lastIndexOf("/")+1,a.length));0<=a.indexOf("dai.ly")&&(c="dailymotion",b=a.substring(a.lastIndexOf("/")+1,a.length));0<=a.indexOf("dailymotion")&&(c="dailymotion",0<=a.indexOf("\x3c/iframe\x3e")?(b=a.substring(a.indexOf("dailymotion.com/")+16,a.indexOf("\x3e\x3c/iframe\x3e")),b=b.substring(b.lastIndexOf("/")+
1,b.lastIndexOf('"'))):b=0<=a.indexOf("_")?a.substring(a.lastIndexOf("/")+1,a.indexOf("_")):a.substring(a.lastIndexOf("/")+1,a.length));return{reproductor:c,id_video:b}};