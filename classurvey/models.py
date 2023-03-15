from django.db import models


# sounds for testing
class TestSound(models.Model):
    sound_id = models.CharField(max_length=50)
    sound_class = models.CharField(max_length=50)

    def __str__(self):
        return f"<TestSound {self.sound_id}>"
    

# store data
class SoundAnswer(models.Model):
    # should be foreign key
    user_id = models.CharField(max_length=50)  # this can be FS ID or IP ADDRESS
    test_sound = models.ForeignKey(TestSound, on_delete=models.CASCADE)
    # available choices, test for now with few
    test_choices =(
        ("m-p", "Percussion"),
        ("m-si","Solo"),
        ("m-ms", "Multi"),
        ("m-other", "Other"),

        ("i-p","Percussion"),
        ("i-s","Wind"),
        ("i-w","String"),
        ("i-t","resttt"),
        ("i-e","Synth / Electronic"),
        ("i-other", "Other"),

        ("sp-s", "Solo"),
        ("sp-co", "Conversation"),
        ("sp-cr", "Crowd"),
        ("sp-other", "Other"),

        ("fx-o", "Daily Objects - House Appliances"),
        ("fx-v", "Vehicle sounds"),
        ("fx-m", "Other mechanisms, engines, machines"),
        ("fx-h", "Human sounds"),
        ("fx-a","Animals"),
        ("fx-n","Natural occurrences"),
        ("fx-el","Electronic - Sci-fi"),
        ("fx-experiment","Experimental"),
        ("fx-d","Design"),
        ("fx-other", "Other"),

        ("ss-n","Natural"),
        ("ss-i","Indoors"),
        ("ss-u","Urban"),
        ("ss-s","Synthetic - Artificial"),
        ("ss-other", "Other")
    )
    chosen_class = models.CharField(max_length=15, choices=test_choices, default="")


class ExitInfoModel(models.Model):
    answer = models.CharField(max_length=255)