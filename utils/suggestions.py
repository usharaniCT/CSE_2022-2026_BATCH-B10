def get_suggestions(result):

    suggestions = {

        "normal": """
STAGE: NORMAL (Early Detection)

Description:
The plant shows very small or minimal insect damage. Leaves may have tiny bite marks
or very small discoloration spots. The crop is still healthy and the infestation
has just started.

Recommended Treatment:

1. Inspect plants regularly for insect activity.
2. Remove affected leaves manually if damage is minimal.
3. Spray Neem Oil solution (5 ml per liter of water) once every 7 days.
4. Maintain proper field hygiene by removing weeds.
5. Encourage natural predators like ladybugs and spiders.

Preventive Measures:

• Maintain good irrigation practices.
• Use insect-resistant crop varieties if available.
• Install yellow sticky traps to monitor pest population.
• Avoid excessive nitrogen fertilizers.
""",

        "moderate": """
STAGE: MODERATE DAMAGE

Description:
Leaves show visible holes, chewing marks, or curling. Insects may be clearly
visible on the plant. The infestation has started spreading and can reduce
crop productivity if not controlled.

Recommended Treatment:

1. Spray Neem Oil or Botanical Pesticide twice a week.
2. Apply biological control agents like Bacillus thuringiensis (Bt).
3. Remove heavily damaged leaves to stop spread.
4. Use pheromone traps to reduce pest population.
5. Spray soap water solution (10 ml liquid soap per liter water).

Chemical Control (if necessary):

• Use Imidacloprid or Spinosad spray as recommended by agricultural experts.

Preventive Measures:

• Regular field monitoring.
• Crop rotation.
• Avoid water stagnation around plants.
""",

        "severe": """
STAGE: SEVERE DAMAGE

Description:
Large areas of leaves are destroyed or skeletonized. Insects are heavily
present and the crop health is severely affected. Yield loss is very likely
if treatment is delayed.

Recommended Treatment:

1. Immediately remove heavily infected area.
2. Apply strong biological pesticides like Bacillus thuringiensis.
3. Spray recommended insecticides such as:
   - Spinosad
   - Chlorpyrifos
   - Imidacloprid

4. Repeat pesticide application every 5–7 days if infestation persists.
5. Use pheromone traps and light traps to reduce pest population.

Emergency Control Measures:

• Apply systemic insecticides as per agricultural guidelines.
• Consult local agricultural extension services for proper dosage.

Preventive Measures:

• Deep ploughing after harvest.
• Maintain proper crop spacing.
• Destroy infected plant residues.
• Implement Integrated Pest Management (IPM).
"""
    }

    return suggestions.get(result.lower(), "No suggestions available.")