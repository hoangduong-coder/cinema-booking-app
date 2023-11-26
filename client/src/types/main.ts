export interface Movie {
  id: number,
  name: string,
  length: number,
  release_date: string,
  language: string,
  genre: Array<string>
  poster?: string
}

export interface Cinema {
  id: number,
  name: string,
  city: string,
  number_of_auditoriums: number
}

export interface Screening {
  id: number,
  cinema_id: number,
  auditorium: number,
  start_time: string
  movie_id: number
}