# Bird Watching Field Notes

Repo for code and output from bird watching field notes. The compiled output is located [here](output/field_notes.md).

The full pipeline consists of the following:
1. Extract the text from the scanned images (not done here)
2. Standardize spelling and case (GPT API call)
3. Automatic match to an entry in eBird (eBird API call)
4. Manual processing of remaining entries, and
5. Final disambiguation, association of Scientific name, link to eBird

A few sample rows of the output is below:

| Date        | Time   | Location   | Weather    | Name from Notes           | Common Name                               | Seen/Heard     | Count   | Male/Female   | Comments   | Scientific Name           | eBird URL                                                                                                       |
|:------------|:-------|:-----------|:-----------|:--------------------------|:------------------------------------------|:---------------|:--------|:--------------|:-----------|:--------------------------|:----------------------------------------------------------------------------------------------------------------|
| 07 Dec 1997 |        |            | Cloudy Sky | White Headed Babbler      | Yellow-billed Babbler                     | Seen           |         |               |            | Argya affinis             | =HYPERLINK("https://ebird.org/species/yebbab1?siteLanguage=en_IN", "Yellow-billed Babbler")                     |
|             |        |            |            | White Browed Bulbul       | White-browed Bulbul                       | Heard          |         |               |            | Pycnonotus luteolus       | =HYPERLINK("https://ebird.org/species/whbbul2?siteLanguage=en_IN", "White-browed Bulbul")                       |
|             |        |            |            | Rose Ringed Parakeet      | Rose-ringed Parakeet                      | Seen And Heard |         |               |            | Psittacula krameri        | =HYPERLINK("https://ebird.org/species/rorpar?siteLanguage=en_IN", "Rose-ringed Parakeet")                       |
|             |        |            |            | Pond Heron                | Indian Pond-Heron                         | Seen And Heard |         |               |            | Ardeola grayii            | =HYPERLINK("https://ebird.org/species/inpher1?siteLanguage=en_IN", "Indian Pond-Heron")                         |
|             |        |            |            | Koel                      | Asian Koel                                | Seen And Heard |         |               |            | Eudynamys scolopaceus     | =HYPERLINK("https://ebird.org/species/asikoe2?siteLanguage=en_IN", "Asian Koel")                                |
|             |        |            |            | Coucal                    | Greater Coucal                            | Heard          |         |               |            | Centropus sinensis        | =HYPERLINK("https://ebird.org/species/grecou1?siteLanguage=en_IN", "Greater Coucal")                            |
|             |        |            |            | Spotted Dove              | Spotted Dove                              | Seen And Heard |         |               |            | Spilopelia chinensis      | =HYPERLINK("https://ebird.org/species/spodov?siteLanguage=en_IN", "Spotted Dove")                               |
|             |        |            |            | White Breasted Kingfisher | White-throated Kingfisher                 |                |         |               |            | Halcyon smyrnensis        | =HYPERLINK("https://ebird.org/species/whtkin2?siteLanguage=en_IN", "White-throated Kingfisher")                 |
|             |        |            |            | Drongo                    | Hair-crested Drongo (Spangled Drongo)     |                |         |               |            | Dicrurus hottentottus     | =HYPERLINK("https://ebird.org/species/hacdro1?siteLanguage=en_IN", "Hair-crested Drongo (Spangled Drongo)")     |
|             |        |            |            | Pled Waggtail             | White-browed Wagtail (Large Pied Wagtail) | Seen           |         |               |            | Motacilla maderaspatensis | =HYPERLINK("https://ebird.org/species/whbwag1?siteLanguage=en_IN", "White-browed Wagtail (Large Pied Wagtail)") |



