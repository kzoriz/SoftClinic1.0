

function btn_distal(){
    const btn_distal = window.document.getElementById('distal');
    const btn_oclusal = window.document.getElementById('oclusal');
    const btn_lingual = window.document.getElementById('lingual');
    const btn_mesial = window.document.getElementById('mesial');
    const btn_vestibular = window.document.getElementById('vestibular');

    const display_distal = window.document.getElementById('display_distal');
    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_mesial = window.document.getElementById('display_mesial');
    const display_lingual = window.document.getElementById('display_lingual');
    const display_vestibular = window.document.getElementById('display_vestibular');

    display_distal.style.display = 'flex';
    display_oclusal.style.display = 'none';
    display_mesial.style.display = 'none';
    display_lingual.style.display = 'none';
    display_vestibular.style.display = 'none';


    btn_distal.style.background = 'rgb(35,167,240)';
    btn_distal.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    btn_oclusal.style.background = '#ffffff';
    btn_oclusal.style.boxShadow = 'none';

    btn_lingual.style.background = '#ffffff';
    btn_lingual.style.boxShadow = 'none';

    btn_mesial.style.background = '#ffffff';
    btn_mesial.style.boxShadow = 'none';

    btn_vestibular.style.background = '#ffffff';
    btn_vestibular.style.boxShadow = 'none';

}
function btn_oclusal(){
    const btn_distal = window.document.getElementById('distal');
    const btn_oclusal = window.document.getElementById('oclusal');
    const c = window.document.getElementById('lingual');
    const d = window.document.getElementById('mesial');
    const e = window.document.getElementById('vestibular');

    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_distal = window.document.getElementById('display_distal');
    const display_mesial = window.document.getElementById('display_mesial');
    const display_lingual = window.document.getElementById('display_lingual');
    const display_vestibular = window.document.getElementById('display_vestibular');

    display_oclusal.style.display = 'flex';
    display_distal.style.display = 'none';
    display_mesial.style.display = 'none';
    display_lingual.style.display = 'none';
    display_vestibular.style.display = 'none';



    btn_distal.style.background = 'rgb(255, 255, 255)';
    btn_distal.style.boxShadow = 'none';

    btn_oclusal.style.background = 'rgb(35,167,240)';
    btn_oclusal.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    c.style.background = 'rgb(255, 255, 255)';
    c.style.boxShadow = 'none';

    d.style.background = 'rgb(255, 255, 255)';
    d.style.boxShadow = 'none';

    e.style.background = 'rgb(255, 255, 255)';
    e.style.boxShadow = 'none';

}
function btn_mesial(){
    const a = window.document.getElementById('distal');
    const b = window.document.getElementById('oclusal');
    const c = window.document.getElementById('lingual');
    const d = window.document.getElementById('mesial');
    const e = window.document.getElementById('vestibular');

    const display_mesial = window.document.getElementById('display_mesial');
    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_distal = window.document.getElementById('display_distal');
    const display_lingual = window.document.getElementById('display_lingual');
    const display_vestibular = window.document.getElementById('display_vestibular');

    display_oclusal.style.display = 'none';
    display_distal.style.display = 'none';
    display_mesial.style.display = 'flex';
    display_lingual.style.display = 'none';
    display_vestibular.style.display = 'none';



    a.style.background = 'rgb(255, 255, 255)';
    a.style.boxShadow = 'none';

    b.style.background = 'rgb(255, 255, 255)';
    b.style.boxShadow = 'none';

    c.style.background = 'rgb(255, 255, 255)';
    c.style.boxShadow = 'none';

    d.style.background = 'rgb(35,167,240)';
    d.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    e.style.background = '#ffffff';
    e.style.boxShadow = 'none';

 }


 function btn_lingual(){
    const a = window.document.getElementById('distal');
    const b = window.document.getElementById('oclusal');
    const c = window.document.getElementById('lingual');
    const d = window.document.getElementById('mesial');
    const e = window.document.getElementById('vestibular');

    const display_mesial = window.document.getElementById('display_mesial');
    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_distal = window.document.getElementById('display_distal');
    const display_lingual = window.document.getElementById('display_lingual');
    const display_vestibular = window.document.getElementById('display_vestibular');

    display_oclusal.style.display = 'none';
    display_distal.style.display = 'none';
    display_mesial.style.display = 'none';
    display_lingual.style.display = 'flex';
    display_vestibular.style.display = 'none';

    a.style.background = 'rgb(255, 255, 255)';
    a.style.boxShadow = 'none';

    b.style.background = 'rgb(255, 255, 255)';
    b.style.boxShadow = 'none';

    d.style.background = 'rgb(255, 255, 255)';
    d.style.boxShadow = 'none';

    c.style.background = 'rgb(35,167,240)';
    c.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    e.style.background = 'rgb(255, 255, 255)';
    e.style.boxShadow = 'none';

 }
 function btn_vestibular(){
    const a = window.document.getElementById('distal');
    const b = window.document.getElementById('oclusal');
    const c = window.document.getElementById('lingual');
    const d = window.document.getElementById('mesial');
    const e = window.document.getElementById('vestibular');

    const display_mesial = window.document.getElementById('display_mesial');
    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_distal = window.document.getElementById('display_distal');
    const display_lingual = window.document.getElementById('display_lingual');
    const display_vestibular = window.document.getElementById('display_vestibular');

    display_oclusal.style.display = 'none';
    display_distal.style.display = 'none';
    display_mesial.style.display = 'none';
    display_lingual.style.display = 'none';
    display_vestibular.style.display = 'flex';

    a.style.background = 'rgb(255, 255, 255)';
    a.style.boxShadow = 'none';

    b.style.background = 'rgb(255, 255, 255)';
    b.style.boxShadow = 'none';

    d.style.background = 'rgb(255, 255, 255)';
    d.style.boxShadow = 'none';

    e.style.background = 'rgb(35,167,240)';
    e.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    c.style.background = 'rgb(255, 255, 255)';
    c.style.boxShadow = 'none';

 }