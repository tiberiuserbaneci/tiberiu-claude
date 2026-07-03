# VEO PROMPTING SKILL (in-repo, operator 2026-07-03)

Built from Google DeepMind's Veo guide + pro image-to-video workflows. Use for every Ultron reel clip.

## The rule that fixes "labartat / muddy / too big"
- **ONE primary camera move per clip.** Never stack push-in + orbit + crane + cuts in one gen — that is
  exactly what makes Veo output sprawling and messy. Pick ONE: slow push-in (dolly), OR slow drift, OR
  slow crane-down. 2 modifiers max.
- **Specify framing.** Say the shot size (medium / close-up). "Too big" = no framing given → Veo fills
  chaotically. Give a contained, composed frame.
- **100-150 words, 3-6 sentences.** More = muddy.

## The rule that fixes "logo doesn't appear"
- **Veo text-to-video does NOT render brand logos or exact wordmarks faithfully.** Never rely on it.
- **Use IMAGE-TO-VIDEO from a designed SEED frame.** The seed carries the real Claude logo (the
  `claude_official.png` sunburst), the CLAUDE/FABLE wordmarks, the duotone scene, the exact framing.
  Veo only ANIMATES it. Logo guaranteed, framing controlled. (Pro workflow: "the base image is
  everything; output quality is constrained by the input image.")

## Prompt structure (DeepMind 5-part), for the MOTION only
`Camera move + Subject + Action + Context + Style/ambiance`
- Camera: one move ("slow cinematic push-in").
- Action: what animates inside the seed ("code streams line by line, glow pulses gently").
- Style: "duotone charcoal + copper, film grain, shallow depth of field, premium, continuous".
- Add "do not add new objects, keep composition" to stop Veo from re-inventing/sprawling.

## Ultron reel spec
- 9:16 vertical seed (start vertical for Reels).
- Duotone charcoal + copper (the Duotone reference), NO blue/green, NO sci-fi plasma.
- Subject = agentic Claude from the terminal: code + a UI that assembles itself (self-designing).
- Real Claude sunburst + CLAUDE + FABLE present in the seed (so visible from second 1).
- Veo ≥13s (extend) for the no-loop reel; single-move camera.
