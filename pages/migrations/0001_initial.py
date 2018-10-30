# Generated by Django 2.1 on 2018-10-30 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('是否展示', models.BooleanField(default=True)),
                ('上传图片', models.ImageField(blank=True, null=True, upload_to='static/imgs')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/imgs')),
                ('标题', models.CharField(max_length=255)),
                ('地址', models.CharField(max_length=255)),
                ('邮箱', models.CharField(max_length=255)),
                ('电话', models.CharField(max_length=255)),
                ('手机', models.CharField(max_length=255)),
                ('关于我们', models.CharField(max_length=255)),
                ('微信', models.CharField(blank=True, max_length=255)),
                ('微博', models.CharField(blank=True, max_length=255)),
                ('QQ', models.CharField(blank=True, max_length=255)),
                ('淘宝', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OurProductCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('产品分类', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Choiceus',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('图标', models.CharField(max_length=255)),
                ('选择原因', models.CharField(max_length=255)),
                ('选择原因标题', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('客户头像', models.CharField(max_length=255)),
                ('客户姓名', models.CharField(max_length=255)),
                ('客户职位', models.CharField(max_length=255)),
                ('客户描述', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('公司地址', models.CharField(max_length=255)),
                ('电话号码', models.CharField(max_length=255)),
                ('电子邮件', models.CharField(max_length=255)),
                ('信息描述', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('分享链接', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('消息内容', models.CharField(max_length=255)),
                ('消息标题', models.CharField(max_length=255)),
                ('时间', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurAdvantage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('优点描述', models.CharField(max_length=255)),
                ('优点分类', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurGood',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('擅长的领域描述', models.CharField(max_length=255)),
                ('擅长的领域分类', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurGuidance',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('业务类型', models.CharField(max_length=255)),
                ('业务描述', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurGuidances',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('图标', models.CharField(max_length=255)),
                ('服务类型', models.CharField(max_length=255)),
                ('指导描述', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurPartners',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurProduct',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('产品名字', models.CharField(max_length=255)),
                ('产品描述', models.CharField(max_length=255)),
                ('产品分类', models.CharField(max_length=255)),
                ('产品属性', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('口号', models.CharField(max_length=255)),
                ('服务类型', models.CharField(max_length=255)),
                ('服务描述', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('团队人员姓名', models.CharField(max_length=255)),
                ('团队人员职位', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.BaseModel')),
                ('口号', models.CharField(max_length=255)),
                ('响亮口号', models.CharField(max_length=255)),
                ('使命', models.CharField(max_length=255)),
            ],
            bases=('pages.basemodel',),
        ),
    ]