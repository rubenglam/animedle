import { Anime } from '@/types'
import Image from 'next/image'
import Link from 'next/link'

interface Props {
  anime: Anime
}

export function AnimeSelectorCard({ anime }: Props) {
  return (
    <Link href={`/${anime.link}`}>
      <article className='flex flex-col gap-2 cursor-pointer w-52 h-80'>
        <Image src={anime.image} alt={anime.title} width={160} height={160} className='border rounded-lg aspect-square h-full w-full' />
        <h3 className='text-center font-bold text-lg uppercase text-black hover:underline underline-offset-4'>{anime.title}</h3>
      </article>
    </Link>
  )
}
