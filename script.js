const screens={
 capture:{description:'Keep a note close to your tasks and current project.',alt:'Pencil browser demo: Today view with tasks, a note field and the current project.'},
 context:{description:'Follow a decision back to its notes and supporting sources.',alt:'Pencil browser demo: Atlas launch knowledge page with decisions and links to source notes.'},
 'next-step':{description:'Bring the commitments in your notes into a task list.',alt:'Pencil browser demo: tasks from the Atlas launch meeting notes.'}
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
