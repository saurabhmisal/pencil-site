const memories = {
  decision: {
    title: 'A smaller launch makes room to learn.',
    text: 'The team chose a pilot before a wider release to understand where first-time users get stuck. The goal was to learn from onboarding before expanding access.',
    source: 'Planning notes',
    quote: '“Start with a small pilot. Watch the first session, fix the rough edges, then decide when to open access.”'
  },
  changed: {
    title: 'The first session became the priority.',
    text: 'The initial plan focused on adding more features. Research in this fictional project shifted the emphasis to helping people complete their first useful task, so the team narrowed the pilot.',
    source: 'Research summary',
    quote: '“Participants could find the features, but were unsure where to begin. Prioritize a clear first task before adding more options.”'
  },
  next: {
    title: 'The wider release is still an open decision.',
    text: 'The pilot comes first. Before expanding access, the team needs to review onboarding observations and agree which rough edges to fix. The checklist does not set a wider release date.',
    source: 'Launch checklist',
    quote: '“Next: review pilot sessions, agree the onboarding fixes, and revisit the wider release. Release date: undecided.”'
  }
};

const questionButtons = document.querySelectorAll('[data-question]');
const sourceToggle = document.querySelector('#source-toggle');
const sourceDetail = document.querySelector('#source-detail');

for (const questionButton of questionButtons) {
  questionButton.addEventListener('click', () => {
    const memory = memories[questionButton.dataset.question];
    for (const sibling of questionButtons) sibling.setAttribute('aria-pressed', String(sibling === questionButton));
    document.querySelector('#answer-title').textContent = memory.title;
    document.querySelector('#answer-text').textContent = memory.text;
    sourceToggle.textContent = `${memory.source} ↗`;
    sourceToggle.setAttribute('aria-expanded', 'false');
    sourceDetail.hidden = true;
    document.querySelector('#source-heading').textContent = `${memory.source.toUpperCase()} · FICTIONAL EXCERPT`;
    document.querySelector('#source-quote').textContent = memory.quote;
  });
}

sourceToggle.addEventListener('click', () => {
  const expanded = sourceToggle.getAttribute('aria-expanded') === 'true';
  sourceToggle.setAttribute('aria-expanded', String(!expanded));
  sourceDetail.hidden = expanded;
});
