PortugueseStemmer=function(){var r=new BaseStemmer;var e=[["",-1,3],["ã",0,1],["õ",0,2]];var i=[["",-1,3],["a~",0,1],["o~",0,2]];var s=[["ic",-1,-1],["ad",-1,-1],["os",-1,-1],["iv",-1,1]];var a=[["ante",-1,1],["avel",-1,1],["ível",-1,1]];var u=[["ic",-1,1],["abil",-1,1],["iv",-1,1]];var o=[["ica",-1,1],["ância",-1,1],["ência",-1,4],["logia",-1,2],["ira",-1,9],["adora",-1,1],["osa",-1,1],["ista",-1,1],["iva",-1,8],["eza",-1,1],["idade",-1,7],["ante",-1,1],["mente",-1,6],["amente",12,5],["ável",-1,1],["ível",-1,1],["ico",-1,1],["ismo",-1,1],["oso",-1,1],["amento",-1,1],["imento",-1,1],["ivo",-1,8],["aça~o",-1,1],["uça~o",-1,3],["ador",-1,1],["icas",-1,1],["ências",-1,4],["logias",-1,2],["iras",-1,9],["adoras",-1,1],["osas",-1,1],["istas",-1,1],["ivas",-1,8],["ezas",-1,1],["idades",-1,7],["adores",-1,1],["antes",-1,1],["aço~es",-1,1],["uço~es",-1,3],["icos",-1,1],["ismos",-1,1],["osos",-1,1],["amentos",-1,1],["imentos",-1,1],["ivos",-1,8]];var t=[["ada",-1,1],["ida",-1,1],["ia",-1,1],["aria",2,1],["eria",2,1],["iria",2,1],["ara",-1,1],["era",-1,1],["ira",-1,1],["ava",-1,1],["asse",-1,1],["esse",-1,1],["isse",-1,1],["aste",-1,1],["este",-1,1],["iste",-1,1],["ei",-1,1],["arei",16,1],["erei",16,1],["irei",16,1],["am",-1,1],["iam",20,1],["ariam",21,1],["eriam",21,1],["iriam",21,1],["aram",20,1],["eram",20,1],["iram",20,1],["avam",20,1],["em",-1,1],["arem",29,1],["erem",29,1],["irem",29,1],["assem",29,1],["essem",29,1],["issem",29,1],["ado",-1,1],["ido",-1,1],["ando",-1,1],["endo",-1,1],["indo",-1,1],["ara~o",-1,1],["era~o",-1,1],["ira~o",-1,1],["ar",-1,1],["er",-1,1],["ir",-1,1],["as",-1,1],["adas",47,1],["idas",47,1],["ias",47,1],["arias",50,1],["erias",50,1],["irias",50,1],["aras",47,1],["eras",47,1],["iras",47,1],["avas",47,1],["es",-1,1],["ardes",58,1],["erdes",58,1],["irdes",58,1],["ares",58,1],["eres",58,1],["ires",58,1],["asses",58,1],["esses",58,1],["isses",58,1],["astes",58,1],["estes",58,1],["istes",58,1],["is",-1,1],["ais",71,1],["eis",71,1],["areis",73,1],["ereis",73,1],["ireis",73,1],["áreis",73,1],["éreis",73,1],["íreis",73,1],["ásseis",73,1],["ésseis",73,1],["ísseis",73,1],["áveis",73,1],["íeis",73,1],["aríeis",84,1],["eríeis",84,1],["iríeis",84,1],["ados",-1,1],["idos",-1,1],["amos",-1,1],["áramos",90,1],["éramos",90,1],["íramos",90,1],["ávamos",90,1],["íamos",90,1],["aríamos",95,1],["eríamos",95,1],["iríamos",95,1],["emos",-1,1],["aremos",99,1],["eremos",99,1],["iremos",99,1],["ássemos",99,1],["êssemos",99,1],["íssemos",99,1],["imos",-1,1],["armos",-1,1],["ermos",-1,1],["irmos",-1,1],["ámos",-1,1],["arás",-1,1],["erás",-1,1],["irás",-1,1],["eu",-1,1],["iu",-1,1],["ou",-1,1],["ará",-1,1],["erá",-1,1],["irá",-1,1]];var c=[["a",-1,1],["i",-1,1],["o",-1,1],["os",-1,1],["á",-1,1],["í",-1,1],["ó",-1,1]];var f=[["e",-1,1],["ç",-1,2],["é",-1,1],["ê",-1,1]];var l=[17,65,16,0,0,0,0,0,0,0,0,0,0,0,0,0,3,19,12,2];var n=0;var m=0;var b=0;function k(){var i;while(true){var s=r.cursor;r:{r.bra=r.cursor;i=r.find_among(e);if(i==0){break r}r.ket=r.cursor;switch(i){case 1:if(!r.slice_from("a~")){return false}break;case 2:if(!r.slice_from("o~")){return false}break;case 3:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=s;break}return true}function _(){b=r.limit;m=r.limit;n=r.limit;var e=r.cursor;r:{e:{var i=r.cursor;i:{if(!r.in_grouping(l,97,250)){break i}s:{var s=r.cursor;a:{if(!r.out_grouping(l,97,250)){break a}u:while(true){o:{if(!r.in_grouping(l,97,250)){break o}break u}if(r.cursor>=r.limit){break a}r.cursor++}break s}r.cursor=s;if(!r.in_grouping(l,97,250)){break i}a:while(true){u:{if(!r.out_grouping(l,97,250)){break u}break a}if(r.cursor>=r.limit){break i}r.cursor++}}break e}r.cursor=i;if(!r.out_grouping(l,97,250)){break r}i:{var a=r.cursor;s:{if(!r.out_grouping(l,97,250)){break s}a:while(true){u:{if(!r.in_grouping(l,97,250)){break u}break a}if(r.cursor>=r.limit){break s}r.cursor++}break i}r.cursor=a;if(!r.in_grouping(l,97,250)){break r}if(r.cursor>=r.limit){break r}r.cursor++}}b=r.cursor}r.cursor=e;var u=r.cursor;r:{e:while(true){i:{if(!r.in_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}m=r.cursor;e:while(true){i:{if(!r.in_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}n=r.cursor}r.cursor=u;return true}function v(){var e;while(true){var s=r.cursor;r:{r.bra=r.cursor;e=r.find_among(i);if(e==0){break r}r.ket=r.cursor;switch(e){case 1:if(!r.slice_from("ã")){return false}break;case 2:if(!r.slice_from("õ")){return false}break;case 3:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=s;break}return true}function d(){if(!(b<=r.cursor)){return false}return true}function g(){if(!(m<=r.cursor)){return false}return true}function w(){if(!(n<=r.cursor)){return false}return true}function h(){var e;r.ket=r.cursor;e=r.find_among_b(o);if(e==0){return false}r.bra=r.cursor;switch(e){case 1:if(!w()){return false}if(!r.slice_del()){return false}break;case 2:if(!w()){return false}if(!r.slice_from("log")){return false}break;case 3:if(!w()){return false}if(!r.slice_from("u")){return false}break;case 4:if(!w()){return false}if(!r.slice_from("ente")){return false}break;case 5:if(!g()){return false}if(!r.slice_del()){return false}var i=r.limit-r.cursor;r:{r.ket=r.cursor;e=r.find_among_b(s);if(e==0){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}switch(e){case 1:r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}break}}break;case 6:if(!w()){return false}if(!r.slice_del()){return false}var t=r.limit-r.cursor;r:{r.ket=r.cursor;if(r.find_among_b(a)==0){r.cursor=r.limit-t;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-t;break r}if(!r.slice_del()){return false}}break;case 7:if(!w()){return false}if(!r.slice_del()){return false}var c=r.limit-r.cursor;r:{r.ket=r.cursor;if(r.find_among_b(u)==0){r.cursor=r.limit-c;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-c;break r}if(!r.slice_del()){return false}}break;case 8:if(!w()){return false}if(!r.slice_del()){return false}var f=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-f;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-f;break r}if(!r.slice_del()){return false}}break;case 9:if(!d()){return false}if(!r.eq_s_b("e")){return false}if(!r.slice_from("ir")){return false}break}return true}function p(){if(r.cursor<b){return false}var e=r.limit_backward;r.limit_backward=b;r.ket=r.cursor;if(r.find_among_b(t)==0){r.limit_backward=e;return false}r.bra=r.cursor;if(!r.slice_del()){return false}r.limit_backward=e;return true}function q(){r.ket=r.cursor;if(r.find_among_b(c)==0){return false}r.bra=r.cursor;if(!d()){return false}if(!r.slice_del()){return false}return true}function z(){var e;r.ket=r.cursor;e=r.find_among_b(f);if(e==0){return false}r.bra=r.cursor;switch(e){case 1:if(!d()){return false}if(!r.slice_del()){return false}r.ket=r.cursor;r:{var i=r.limit-r.cursor;e:{if(!r.eq_s_b("u")){break e}r.bra=r.cursor;var s=r.limit-r.cursor;if(!r.eq_s_b("g")){break e}r.cursor=r.limit-s;break r}r.cursor=r.limit-i;if(!r.eq_s_b("i")){return false}r.bra=r.cursor;var a=r.limit-r.cursor;if(!r.eq_s_b("c")){return false}r.cursor=r.limit-a}if(!d()){return false}if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("c")){return false}break}return true}this.stem=function(){var e=r.cursor;k();r.cursor=e;_();r.limit_backward=r.cursor;r.cursor=r.limit;var i=r.limit-r.cursor;r:{e:{var s=r.limit-r.cursor;i:{var a=r.limit-r.cursor;s:{var u=r.limit-r.cursor;a:{if(!h()){break a}break s}r.cursor=r.limit-u;if(!p()){break i}}r.cursor=r.limit-a;var o=r.limit-r.cursor;s:{r.ket=r.cursor;if(!r.eq_s_b("i")){break s}r.bra=r.cursor;var t=r.limit-r.cursor;if(!r.eq_s_b("c")){break s}r.cursor=r.limit-t;if(!d()){break s}if(!r.slice_del()){return false}}r.cursor=r.limit-o;break e}r.cursor=r.limit-s;if(!q()){break r}}}r.cursor=r.limit-i;var c=r.limit-r.cursor;z();r.cursor=r.limit-c;r.cursor=r.limit_backward;var f=r.cursor;v();r.cursor=f;return true};this["stemWord"]=function(e){r.setCurrent(e);this.stem();return r.getCurrent()}};