from gettext import gettext as _

""" Content Kind Constants """
# constants for ContentKind
CK_TOPIC = "topic"
CK_VIDEO = "video"
CK_AUDIO = "audio"
CK_EXERCISE = "exercise"
CK_DOCUMENT = "document"

kind_choices = (
    (CK_TOPIC, _("Topic")),
    (CK_VIDEO, _("Video")),
    (CK_AUDIO, _("Audio")),
    (CK_EXERCISE, _("Exercise")),
    (CK_DOCUMENT, _("Document")),
)


""" File Format Constants """
# constants for Video format
FF_MP4 = "mp4"
# constants for Subtitle format
FF_VTT = "vtt"
FF_SRT = "srt"

# constants for Audio format
FF_MP3 = "mp3"
FF_WAV = "wav"

# constants for Document format
FF_PDF = "pdf"

# constants for Thumbnail format
FF_JPG = "jpg"
FF_JPEG = "jpeg"
FF_PNG = "png"

# constants for Exercise format
FF_PERSEUS = "perseus"

format_choices = (
    (FF_MP4, _("mp4")),

    (FF_VTT, _("vtt")),
    (FF_SRT, _("srt")),

    (FF_MP3, _("mp3")),
    (FF_WAV, _("wav")),

    (FF_PDF, _("pdf")),

    (FF_JPG, _("jpg")),
    (FF_JPEG, _("jpeg")),
    (FF_PNG, _("png")),

    (FF_PERSEUS, _("perseus")),
)


""" License Constants """
L_CC_BY = "CC-BY"
L_CC_BY_SA = "CC BY-SA"
L_CC_BY_ND = "CC BY-ND"
L_CC_BY_NC = "CC BY-NC"
L_CC_BY_NC_SA = "CC BY-NC-SA"
L_CC_BY_NC_ND = "CC BY-NC-ND"
L_ARRD = "All Rights Reserved"
L_PD = "Public Domain"

license_choices = (
    (L_CC_BY, _("CC-BY")),
    (L_CC_BY_SA, _("CC BY-SA")),
    (L_CC_BY_ND, _("CC BY-ND")),
    (L_CC_BY_NC, _("CC BY-NC")),
    (L_CC_BY_NC_SA, _("CC BY-NC-SA")),
    (L_CC_BY_NC_ND, _("CC BY-NC-ND")),
    (L_ARRD, _("All Rights Reserved")),
    (L_PD, _("Public Domain")),
)


""" Format Preset Constants"""
FP_VIDEO_HIGH_RES = "high_res_video"
FP_VIDEO_LOW_RES = "low_res_video"
FP_VIDEO_VECTOR = "vector_video"
FP_VIDEO_THUMBNAIL = "video_thumbnail"
FP_VIDEO_SUBTITLE = "video_subtitle"

FP_AUDIO = "aud"
FP_AUDIO_THUMBNAIL = "audio_thumbnail"

FP_DOCUMENT = "doc"
FP_DOCUMENT_THUMBNAIL = "document_thumbnail"

FP_EXERCISE = "exercise"
FP_EXERCISE_THUMBNAIL = "exercise_thumbnail"

preset_choices = (
    (FP_VIDEO_HIGH_RES, _("High resolution video")),
    (FP_VIDEO_LOW_RES, _("Low resolution video")),
    (FP_VIDEO_VECTOR, _("Vector video")),
    (FP_VIDEO_THUMBNAIL, _("Thumbnail")),
    (FP_VIDEO_SUBTITLE, _("Subtitle")),

    (FP_AUDIO, _("Audio")),
    (FP_AUDIO_THUMBNAIL, _("Thumbnail")),

    (FP_DOCUMENT, _("Document")),
    (FP_DOCUMENT_THUMBNAIL, _("Thumbnail")),

    (FP_EXERCISE, _("Exercise")),
    (FP_EXERCISE_THUMBNAIL, _("Thumbnail")),
)
