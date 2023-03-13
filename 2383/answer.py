class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        minTrainEnergy = -1
        minTrainExperience = -1
        result = 0
        currentEnergy = initialEnergy
        currentExperience = initialExperience
        for i in range(len(energy)):
            # compete with i-th player
            # energy
            if currentEnergy > energy[i]:
                pass
            else:
                minTrainEnergy = max(minTrainEnergy, energy[i] - currentEnergy + 1)
            # experience
            if currentExperience > experience[i]:
                pass
            else:
                minTrainExperience = max(minTrainExperience, experience[i] - currentExperience + 1)
            currentEnergy -= energy[i]
            currentExperience += experience[i]

        if minTrainEnergy > 0:
            result += minTrainEnergy
        if minTrainExperience > 0:
            result += minTrainExperience
        
        return result
