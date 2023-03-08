

export type tournamentType = {
    id: number
    slug: string
    name: string
    date?: string
    location?: string
    url?: string
    notes?: string
}

export type eventType = {
    id: number,
    slug: string,
    name: string,
    date: string,
    weapon: string,
    eventLevel: string,
    notes: string
}

export type boutType = {
    id: number
    slug: string
    winnerIsA: boolean
    fencerA: string
    fencerB: string
    scoreA: number,
    scoreB: number,
    fencerAHand: string
    fencerBHand: string
    fencerAYellowCard: boolean
    fencerBYellowCard: boolean
    fencerARedCard: boolean
    fencerBRedCard: boolean
    fencerABlackCard: boolean
    fencerBBlackCard: boolean
    fencerAPassivity: boolean
    fencerBPassivity: boolean
    fencerAMedical: boolean
    fencerBMedical: boolean
    fencerAVideoUsed: number
    fencerBVideoUsed: number
    fencerAFootwork: string
    fencerBFootwork: string
    fencerABladework: string
    fencerBBladework: string
    fencerADistance: string
    fencerBDistance: string
    fencerATiming: string
    fencerBTiming: string
    fencerAEnergy: string
    fencerBEnergy: string
    fencerANotes: string
    fencerBNotes: string
    referee: string
    boutFormat: string
    round: number
    notes: string
    shareCoach: boolean
    deleted: boolean
}