import { AnimeSelector } from '@/components/anime-selector'

export default function Home() {
  return (
    <div className='min-h-screen flex justify-center items-center font-[family-name:var(--font-geist-sans)]'>
      <main className='flex flex-col gap-8 row-start-2 items-center w-full'>
        <h1 className='text-5xl font-semibold'>Animedle</h1>
        <AnimeSelector />
      </main>
    </div>
  )
}
