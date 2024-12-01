import { ANIMES } from '@/constants/animes'
import { AnimeSelectorCard } from './anime-selector-card'

export function AnimeSelector() {
  return (
    <section className='flex flex-wrap items-center justify-center w-2/3 gap-4 rounded-lg bg-orange-300 p-8'>
      {ANIMES.map(anime => (
        <AnimeSelectorCard key={anime.title} anime={anime} />
      ))}
    </section>
  )
}
