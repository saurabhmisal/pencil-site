const screens={
 dashboard:{description:'See what needs you, what’s next and where you left off.',alt:'Pencil Studio dashboard with tasks, recent conversations and upcoming commitments in a sample workspace.'},
 calendar:{description:'Make room for focused work alongside the rest of your day.',alt:'Pencil Studio calendar showing sample meetings, focus sessions and an agenda.'},
 journal:{description:'Keep a daily thread of thoughts, progress and open loops.',alt:'Pencil Studio daily journal with sample entries and a daily recap.'},
 context:{description:'Return to the notes and decisions behind your next step.',alt:'Pencil Studio connected context with source-linked notes and decisions in a sample workspace.'}
};
const tabs=[...document.querySelectorAll('[data-screen]')];
function select(tab){
 const key=tab.dataset.screen,screen=screens[key];if(!screen)return;
 for(const item of tabs){item.setAttribute('aria-selected',String(item===tab));item.tabIndex=item===tab?0:-1;}
 document.querySelector('#screen-panel').setAttribute('aria-labelledby',tab.id);
 document.querySelector('#screen-description').textContent=screen.description;
 const path=`assets/screenshots/${key}.jpg`,image=document.querySelector('#screen-image');image.src=path;image.alt=screen.alt;
 document.querySelector('#screen-image-link').href=path;
}
for(const [index,tab] of tabs.entries()){
 tab.addEventListener('click',()=>select(tab));
 tab.addEventListener('keydown',event=>{
  if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;
  event.preventDefault();const next=event.key==='Home'?0:event.key==='End'?tabs.length-1:(index+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;
  select(tabs[next]);tabs[next].focus();
 });
}
