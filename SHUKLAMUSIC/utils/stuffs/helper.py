class Helper(object):
    HELP_M = '''اختر الفئة التي تريد الحصول على المساعدة فيها.
اطرح أسئلتك في محادثة الدعم

يمكن استخدام جميع الأوامر مع: /'''

    HELP_ChatGPT = '''شات جي بي تي

أوامر شات جي بي تي:

/ask ➠ يستعلم من نموذج الذكاء الاصطناعي للحصول على إجابة لسؤالك.
'''

    HELP_Sticker = '''الملصقات

أوامر الملصقات:

/packkang ➠ ينشئ حزمة ملصقات من حزمة أخرى.
/stickerid ➠ يحصل على معرف الملصق.
'''

    HELP_TagAll = '''المنشن

أوامر المنشن:

✿ اختر نوع المنشن في مجموعتك ✿

๏ /gmtag ➛ منشن صباح الخير
للإيقاف ⇴ /gmstop

๏ /gntag ➛ منشن مساء الخير
للإيقاف ⇴ /gnstop

๏ /tagall ➛ منشن برسالة عشوائية
للإيقاف ⇴ /tagoff /tagstop

๏ /hitag ➛ منشن برسالة هندية عشوائية
للإيقاف ⇴/histop

๏ /shayari ➛ منشن بشعر عشوائي
للإيقاف ⇴ /shstop

๏ /utag ➛ منشن بنص مخصص
للإيقاف ⇴ /cancel 

๏ /vctag ➛ منشن دعوة للمحادثة الصوتية
للإيقاف ⇴ /vcstop
'''

    HELP_Info = '''المعلومات

أوامر المعلومات:

/id : للحصول على معرف المجموعة الحالية. إذا تم استخدامه بالرد على رسالة، يحصل على معرف المستخدم.
/info : للحصول على معلومات حول المستخدم.
/github <اسم المستخدم> : للحصول على معلومات حول مستخدم جيثب.
'''

    HELP_Group = '''المجموعة

أوامر إدارة المجموعة:

هذه هي الأوامر المتاحة لإدارة المجموعة:

⦿ /pin ➠ تثبيت رسالة في المجموعة.
⦿ /pinned ➠ عرض الرسالة المثبتة في المجموعة.
⦿ /unpin ➠ إلغاء تثبيت الرسالة الحالية.
⦿ /staff ➠ عرض قائمة المشرفين.
⦿ /bots ➠ عرض قائمة البوتات في المجموعة.
⦿ /settitle ➠ تعيين عنوان المجموعة.
⦿ /setdiscription ➠ تعيين وصف المجموعة.
⦿ /setphoto ➠ تعيين صورة المجموعة.
⦿ /removephoto ➠ إزالة صورة المجموعة.
⦿ /zombies ➠ إزالة الحسابات المحذوفة من المجموعة.
⦿ /imposter تشغيل/إيقاف ➠ تشغيل أو إيقاف مراقب المجموعة الذي يخبر عن المستخدمين الذين يغيرون أسماءهم.
'''

    HELP_Extra = '''إضافي

الأوامر الإضافية:

⦿ /math ➠ حل المسائل والمعادلات الرياضية.
⦿ /blackpink ➠ إنشاء شعار بنمط بلاك بينك.
⦿ /carbon ➠ إنشاء صورة كود كاربون من نص برمجي.
⦿ /speedtest ➠ قياس سرعة الإنترنت.
⦿ /reverse ➠ عكس النص المعطى.
⦿ /webss ➠ أخذ لقطة شاشة لموقع ويب.
⦿ /paste ➠ رفع نص إلى السحابة وإعطاء رابط.
⦿ /tgm ➠ رفع صورة (أقل من 5 ميجابايت) إلى السحابة وإعطاء رابط.
⦿ /tr ➠ ترجمة النص.
⦿ /google ➠ البحث عن معلومات على جوجل.
⦿ /stack ➠ البحث عن معلومات برمجية على ستاك أوفرفلو.
'''

    HELP_Image = '''الصور

أوامر الصور:

⦿ /draw ➠ إنشاء رسم بناءً على وصف معين.
⦿ /image ➠ البحث عن صورة بناءً على كلمة مفتاحية.
⦿ /upscale ➠ الرد على صورة لتحسين جودتها.
'''

    HELP_Action = '''الإجراءات

أوامر الحظر والكتم:

» الأوامر المتاحة للحظر والكتم:

 ❍ /kickme: طرد المستخدم الذي أصدر الأمر

للمشرفين فقط:
 ❍ /ban <معرف المستخدم>: حظر مستخدم
 ❍ /sban <معرف المستخدم>: حظر صامت للمستخدم
 ❍ /tban <معرف المستخدم> x(د/س/ي): حظر مؤقت
 ❍ /unban <معرف المستخدم>: إلغاء الحظر
 ❍ /kick <معرف المستخدم>: طرد مستخدم
 ❍ /mute <معرف المستخدم>: كتم مستخدم
 ❍ /tmute <معرف المستخدم> x(د/س/ي): كتم مؤقت
 ❍ /unmute <معرف المستخدم>: إلغاء الكتم
'''

    HELP_Search = '''البحث

أوامر البحث:

• /google <استعلام> : البحث في جوجل
• /anime <استعلام> : البحث في قائمة الأنمي
• /stack <استعلام> : البحث في ستاك أوفرفلو
• /image (/imgs) <استعلام> : البحث عن صور
'''

    HELP_Font = '''الخطوط

مساعدة وحدة الخطوط:

تغيير خط أي نص!

◌ /font [النص]
'''

    HELP_Game = '''الألعاب

ألعاب صغيرة للعب:

◌ /toss [رمي عملة]
◌ /roll [رمي نرد]
◌ /dart [رمي سهم]
◌ /slot [ماكينة القمار]
◌ /bowling [لعبة البولينج]
◌ /basket [لعبة كرة السلة]
◌ /football [لعبة كرة القدم]
'''

    HELP_TG = '''تلغراف

أوامر تلغراف:

إنشاء رابط تلغراف لأي وسائط!

◌ /tgm [الرد على وسائط]
◌ /tgt [الرد على وسائط]
'''

    HELP_Imposter = '''المتنكر

وحدة المتنكر:

◌ /imposter on
◌ /imposter off
'''

    HELP_TD = '''الحقيقة والجرأة

أوامر الحقيقة والجرأة:

◌ /truth : إرسال سؤال حقيقة عشوائي
◌ /dare : إرسال تحدي عشوائي
'''

    HELP_HT = '''الهاشتاج

وحدة الهاشتاج:

◌ /hastag : [النص]
'''

    HELP_TTS = '''تحويل النص إلى كلام

وحدة تحويل النص إلى كلام:

❀ تحويل النص إلى كلام
◌ /tts : [النص]

◌ الاستخدام ➛ تحويل النص إلى صوت
'''

    HELP_Fun = '''المرح

وحدة المرح والتسلية:

◌ /wish : أضف أمنيتك وشاهد احتمالية تحققها!

المزيد من الأوامر:
◌ /sigma [تحقق من مستوى سيجما]
◌ /cute [تحقق من مستوى لطافتك]
◌ /horny [تحقق من مستوى شهوانيتك]
◌ /lesbo [تحقق من مستوى ميولك المثلية]
◌ /depressed [تحقق من مستوى اكتئابك]
◌ /gay [تحقق من مستوى مثليتك]
◌ /rand [تحقق من مستوى عشوائيتك]
◌ /bkl [تحقق من مستوى بكل]
◌ /boobs [تحقق من حجم صدرك]
◌ /dick [تحقق من حجم عضوك]
'''

    HELP_Q = '''الاقتباس

وحدة الاقتباس:

◌ /q : إنشاء اقتباس من الرسالة

◌ /q r : إنشاء اقتباس من الرسالة مع الرد
'''

    fullpromote = {
        'can_change_info': True,
        'can_post_messages': True,
        'can_edit_messages': True,
        'can_delete_messages': True,
        'can_invite_users': True,
        'can_restrict_members': True,
        'can_pin_messages': True,
        'can_promote_members': True,
        'can_manage_chat': True,
    }

    promoteuser = {
        'can_change_info': False,
        'can_post_messages': True,
        'can_edit_messages': True,
        'can_delete_messages': False,
        'can_invite_users': True,
        'can_restrict_members': False,
        'can_pin_messages': False,
        'can_promote_members': False,
        'can_manage_chat': True,
    }
