// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_pubsub_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GooglePubsubBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_pubsub_bundle.proto</summary>
  public static partial class GcpGooglePubsubBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_pubsub_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGooglePubsubBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiJnY3AvZ2NwX2dvb2dsZV9wdWJzdWJfYnVuZGxlLnByb3RvEiRvYWs5LnR5",
            "dGhvbi5nY3AuZ29vZ2xlX3B1YnN1Yl9idW5kbGUaE3NoYXJlZC9zaGFyZWQu",
            "cHJvdG8aFGdjcC9nY3BfcHVic3ViLnByb3RvItcFCgxHb29nbGVQdWJzdWIS",
            "OwoNcHVic3ViX3NjaGVtYRgBIAEoCzIkLm9hazkudHl0aG9uLmdjcC5wdWJz",
            "dWIuUHVic3ViU2NoZW1hEkcKE3B1YnN1Yl9zdWJzY3JpcHRpb24YAiADKAsy",
            "Ki5vYWs5LnR5dGhvbi5nY3AucHVic3ViLlB1YnN1YlN1YnNjcmlwdGlvbhJd",
            "Ch9wdWJzdWJfc3Vic2NyaXB0aW9uX2lhbV9iaW5kaW5nGAMgAygLMjQub2Fr",
            "OS50eXRob24uZ2NwLnB1YnN1Yi5QdWJzdWJTdWJzY3JpcHRpb25JYW1CaW5k",
            "aW5nElsKHnB1YnN1Yl9zdWJzY3JpcHRpb25faWFtX21lbWJlchgEIAMoCzIz",
            "Lm9hazkudHl0aG9uLmdjcC5wdWJzdWIuUHVic3ViU3Vic2NyaXB0aW9uSWFt",
            "TWVtYmVyElsKHnB1YnN1Yl9zdWJzY3JpcHRpb25faWFtX3BvbGljeRgFIAMo",
            "CzIzLm9hazkudHl0aG9uLmdjcC5wdWJzdWIuUHVic3ViU3Vic2NyaXB0aW9u",
            "SWFtUG9saWN5EjkKDHB1YnN1Yl90b3BpYxgGIAEoCzIjLm9hazkudHl0aG9u",
            "LmdjcC5wdWJzdWIuUHVic3ViVG9waWMSTwoYcHVic3ViX3RvcGljX2lhbV9i",
            "aW5kaW5nGAcgAygLMi0ub2FrOS50eXRob24uZ2NwLnB1YnN1Yi5QdWJzdWJU",
            "b3BpY0lhbUJpbmRpbmcSTQoXcHVic3ViX3RvcGljX2lhbV9tZW1iZXIYCCAD",
            "KAsyLC5vYWs5LnR5dGhvbi5nY3AucHVic3ViLlB1YnN1YlRvcGljSWFtTWVt",
            "YmVyEk0KF3B1YnN1Yl90b3BpY19pYW1fcG9saWN5GAkgAygLMiwub2FrOS50",
            "eXRob24uZ2NwLnB1YnN1Yi5QdWJzdWJUb3BpY0lhbVBvbGljeWIGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.Pubsub.GcpPubsubReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GooglePubsubBundle.GooglePubsub), global::Oak9.Tython.Gcp.GooglePubsubBundle.GooglePubsub.Parser, new[]{ "PubsubSchema", "PubsubSubscription", "PubsubSubscriptionIamBinding", "PubsubSubscriptionIamMember", "PubsubSubscriptionIamPolicy", "PubsubTopic", "PubsubTopicIamBinding", "PubsubTopicIamMember", "PubsubTopicIamPolicy" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GooglePubsub : pb::IMessage<GooglePubsub>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GooglePubsub> _parser = new pb::MessageParser<GooglePubsub>(() => new GooglePubsub());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GooglePubsub> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GooglePubsubBundle.GcpGooglePubsubBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GooglePubsub() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GooglePubsub(GooglePubsub other) : this() {
      pubsubSchema_ = other.pubsubSchema_ != null ? other.pubsubSchema_.Clone() : null;
      pubsubSubscription_ = other.pubsubSubscription_.Clone();
      pubsubSubscriptionIamBinding_ = other.pubsubSubscriptionIamBinding_.Clone();
      pubsubSubscriptionIamMember_ = other.pubsubSubscriptionIamMember_.Clone();
      pubsubSubscriptionIamPolicy_ = other.pubsubSubscriptionIamPolicy_.Clone();
      pubsubTopic_ = other.pubsubTopic_ != null ? other.pubsubTopic_.Clone() : null;
      pubsubTopicIamBinding_ = other.pubsubTopicIamBinding_.Clone();
      pubsubTopicIamMember_ = other.pubsubTopicIamMember_.Clone();
      pubsubTopicIamPolicy_ = other.pubsubTopicIamPolicy_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GooglePubsub Clone() {
      return new GooglePubsub(this);
    }

    /// <summary>Field number for the "pubsub_schema" field.</summary>
    public const int PubsubSchemaFieldNumber = 1;
    private global::Oak9.Tython.Gcp.Pubsub.PubsubSchema pubsubSchema_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Pubsub.PubsubSchema PubsubSchema {
      get { return pubsubSchema_; }
      set {
        pubsubSchema_ = value;
      }
    }

    /// <summary>Field number for the "pubsub_subscription" field.</summary>
    public const int PubsubSubscriptionFieldNumber = 2;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscription> _repeated_pubsubSubscription_codec
        = pb::FieldCodec.ForMessage(18, global::Oak9.Tython.Gcp.Pubsub.PubsubSubscription.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscription> pubsubSubscription_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscription>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscription> PubsubSubscription {
      get { return pubsubSubscription_; }
    }

    /// <summary>Field number for the "pubsub_subscription_iam_binding" field.</summary>
    public const int PubsubSubscriptionIamBindingFieldNumber = 3;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamBinding> _repeated_pubsubSubscriptionIamBinding_codec
        = pb::FieldCodec.ForMessage(26, global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamBinding.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamBinding> pubsubSubscriptionIamBinding_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamBinding>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamBinding> PubsubSubscriptionIamBinding {
      get { return pubsubSubscriptionIamBinding_; }
    }

    /// <summary>Field number for the "pubsub_subscription_iam_member" field.</summary>
    public const int PubsubSubscriptionIamMemberFieldNumber = 4;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamMember> _repeated_pubsubSubscriptionIamMember_codec
        = pb::FieldCodec.ForMessage(34, global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamMember.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamMember> pubsubSubscriptionIamMember_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamMember>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamMember> PubsubSubscriptionIamMember {
      get { return pubsubSubscriptionIamMember_; }
    }

    /// <summary>Field number for the "pubsub_subscription_iam_policy" field.</summary>
    public const int PubsubSubscriptionIamPolicyFieldNumber = 5;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamPolicy> _repeated_pubsubSubscriptionIamPolicy_codec
        = pb::FieldCodec.ForMessage(42, global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamPolicy.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamPolicy> pubsubSubscriptionIamPolicy_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamPolicy>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubSubscriptionIamPolicy> PubsubSubscriptionIamPolicy {
      get { return pubsubSubscriptionIamPolicy_; }
    }

    /// <summary>Field number for the "pubsub_topic" field.</summary>
    public const int PubsubTopicFieldNumber = 6;
    private global::Oak9.Tython.Gcp.Pubsub.PubsubTopic pubsubTopic_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Pubsub.PubsubTopic PubsubTopic {
      get { return pubsubTopic_; }
      set {
        pubsubTopic_ = value;
      }
    }

    /// <summary>Field number for the "pubsub_topic_iam_binding" field.</summary>
    public const int PubsubTopicIamBindingFieldNumber = 7;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamBinding> _repeated_pubsubTopicIamBinding_codec
        = pb::FieldCodec.ForMessage(58, global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamBinding.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamBinding> pubsubTopicIamBinding_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamBinding>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamBinding> PubsubTopicIamBinding {
      get { return pubsubTopicIamBinding_; }
    }

    /// <summary>Field number for the "pubsub_topic_iam_member" field.</summary>
    public const int PubsubTopicIamMemberFieldNumber = 8;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamMember> _repeated_pubsubTopicIamMember_codec
        = pb::FieldCodec.ForMessage(66, global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamMember.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamMember> pubsubTopicIamMember_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamMember>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamMember> PubsubTopicIamMember {
      get { return pubsubTopicIamMember_; }
    }

    /// <summary>Field number for the "pubsub_topic_iam_policy" field.</summary>
    public const int PubsubTopicIamPolicyFieldNumber = 9;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamPolicy> _repeated_pubsubTopicIamPolicy_codec
        = pb::FieldCodec.ForMessage(74, global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamPolicy.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamPolicy> pubsubTopicIamPolicy_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamPolicy>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Pubsub.PubsubTopicIamPolicy> PubsubTopicIamPolicy {
      get { return pubsubTopicIamPolicy_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GooglePubsub);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GooglePubsub other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(PubsubSchema, other.PubsubSchema)) return false;
      if(!pubsubSubscription_.Equals(other.pubsubSubscription_)) return false;
      if(!pubsubSubscriptionIamBinding_.Equals(other.pubsubSubscriptionIamBinding_)) return false;
      if(!pubsubSubscriptionIamMember_.Equals(other.pubsubSubscriptionIamMember_)) return false;
      if(!pubsubSubscriptionIamPolicy_.Equals(other.pubsubSubscriptionIamPolicy_)) return false;
      if (!object.Equals(PubsubTopic, other.PubsubTopic)) return false;
      if(!pubsubTopicIamBinding_.Equals(other.pubsubTopicIamBinding_)) return false;
      if(!pubsubTopicIamMember_.Equals(other.pubsubTopicIamMember_)) return false;
      if(!pubsubTopicIamPolicy_.Equals(other.pubsubTopicIamPolicy_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (pubsubSchema_ != null) hash ^= PubsubSchema.GetHashCode();
      hash ^= pubsubSubscription_.GetHashCode();
      hash ^= pubsubSubscriptionIamBinding_.GetHashCode();
      hash ^= pubsubSubscriptionIamMember_.GetHashCode();
      hash ^= pubsubSubscriptionIamPolicy_.GetHashCode();
      if (pubsubTopic_ != null) hash ^= PubsubTopic.GetHashCode();
      hash ^= pubsubTopicIamBinding_.GetHashCode();
      hash ^= pubsubTopicIamMember_.GetHashCode();
      hash ^= pubsubTopicIamPolicy_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (pubsubSchema_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(PubsubSchema);
      }
      pubsubSubscription_.WriteTo(output, _repeated_pubsubSubscription_codec);
      pubsubSubscriptionIamBinding_.WriteTo(output, _repeated_pubsubSubscriptionIamBinding_codec);
      pubsubSubscriptionIamMember_.WriteTo(output, _repeated_pubsubSubscriptionIamMember_codec);
      pubsubSubscriptionIamPolicy_.WriteTo(output, _repeated_pubsubSubscriptionIamPolicy_codec);
      if (pubsubTopic_ != null) {
        output.WriteRawTag(50);
        output.WriteMessage(PubsubTopic);
      }
      pubsubTopicIamBinding_.WriteTo(output, _repeated_pubsubTopicIamBinding_codec);
      pubsubTopicIamMember_.WriteTo(output, _repeated_pubsubTopicIamMember_codec);
      pubsubTopicIamPolicy_.WriteTo(output, _repeated_pubsubTopicIamPolicy_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (pubsubSchema_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(PubsubSchema);
      }
      pubsubSubscription_.WriteTo(ref output, _repeated_pubsubSubscription_codec);
      pubsubSubscriptionIamBinding_.WriteTo(ref output, _repeated_pubsubSubscriptionIamBinding_codec);
      pubsubSubscriptionIamMember_.WriteTo(ref output, _repeated_pubsubSubscriptionIamMember_codec);
      pubsubSubscriptionIamPolicy_.WriteTo(ref output, _repeated_pubsubSubscriptionIamPolicy_codec);
      if (pubsubTopic_ != null) {
        output.WriteRawTag(50);
        output.WriteMessage(PubsubTopic);
      }
      pubsubTopicIamBinding_.WriteTo(ref output, _repeated_pubsubTopicIamBinding_codec);
      pubsubTopicIamMember_.WriteTo(ref output, _repeated_pubsubTopicIamMember_codec);
      pubsubTopicIamPolicy_.WriteTo(ref output, _repeated_pubsubTopicIamPolicy_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (pubsubSchema_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(PubsubSchema);
      }
      size += pubsubSubscription_.CalculateSize(_repeated_pubsubSubscription_codec);
      size += pubsubSubscriptionIamBinding_.CalculateSize(_repeated_pubsubSubscriptionIamBinding_codec);
      size += pubsubSubscriptionIamMember_.CalculateSize(_repeated_pubsubSubscriptionIamMember_codec);
      size += pubsubSubscriptionIamPolicy_.CalculateSize(_repeated_pubsubSubscriptionIamPolicy_codec);
      if (pubsubTopic_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(PubsubTopic);
      }
      size += pubsubTopicIamBinding_.CalculateSize(_repeated_pubsubTopicIamBinding_codec);
      size += pubsubTopicIamMember_.CalculateSize(_repeated_pubsubTopicIamMember_codec);
      size += pubsubTopicIamPolicy_.CalculateSize(_repeated_pubsubTopicIamPolicy_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GooglePubsub other) {
      if (other == null) {
        return;
      }
      if (other.pubsubSchema_ != null) {
        if (pubsubSchema_ == null) {
          PubsubSchema = new global::Oak9.Tython.Gcp.Pubsub.PubsubSchema();
        }
        PubsubSchema.MergeFrom(other.PubsubSchema);
      }
      pubsubSubscription_.Add(other.pubsubSubscription_);
      pubsubSubscriptionIamBinding_.Add(other.pubsubSubscriptionIamBinding_);
      pubsubSubscriptionIamMember_.Add(other.pubsubSubscriptionIamMember_);
      pubsubSubscriptionIamPolicy_.Add(other.pubsubSubscriptionIamPolicy_);
      if (other.pubsubTopic_ != null) {
        if (pubsubTopic_ == null) {
          PubsubTopic = new global::Oak9.Tython.Gcp.Pubsub.PubsubTopic();
        }
        PubsubTopic.MergeFrom(other.PubsubTopic);
      }
      pubsubTopicIamBinding_.Add(other.pubsubTopicIamBinding_);
      pubsubTopicIamMember_.Add(other.pubsubTopicIamMember_);
      pubsubTopicIamPolicy_.Add(other.pubsubTopicIamPolicy_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (pubsubSchema_ == null) {
              PubsubSchema = new global::Oak9.Tython.Gcp.Pubsub.PubsubSchema();
            }
            input.ReadMessage(PubsubSchema);
            break;
          }
          case 18: {
            pubsubSubscription_.AddEntriesFrom(input, _repeated_pubsubSubscription_codec);
            break;
          }
          case 26: {
            pubsubSubscriptionIamBinding_.AddEntriesFrom(input, _repeated_pubsubSubscriptionIamBinding_codec);
            break;
          }
          case 34: {
            pubsubSubscriptionIamMember_.AddEntriesFrom(input, _repeated_pubsubSubscriptionIamMember_codec);
            break;
          }
          case 42: {
            pubsubSubscriptionIamPolicy_.AddEntriesFrom(input, _repeated_pubsubSubscriptionIamPolicy_codec);
            break;
          }
          case 50: {
            if (pubsubTopic_ == null) {
              PubsubTopic = new global::Oak9.Tython.Gcp.Pubsub.PubsubTopic();
            }
            input.ReadMessage(PubsubTopic);
            break;
          }
          case 58: {
            pubsubTopicIamBinding_.AddEntriesFrom(input, _repeated_pubsubTopicIamBinding_codec);
            break;
          }
          case 66: {
            pubsubTopicIamMember_.AddEntriesFrom(input, _repeated_pubsubTopicIamMember_codec);
            break;
          }
          case 74: {
            pubsubTopicIamPolicy_.AddEntriesFrom(input, _repeated_pubsubTopicIamPolicy_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (pubsubSchema_ == null) {
              PubsubSchema = new global::Oak9.Tython.Gcp.Pubsub.PubsubSchema();
            }
            input.ReadMessage(PubsubSchema);
            break;
          }
          case 18: {
            pubsubSubscription_.AddEntriesFrom(ref input, _repeated_pubsubSubscription_codec);
            break;
          }
          case 26: {
            pubsubSubscriptionIamBinding_.AddEntriesFrom(ref input, _repeated_pubsubSubscriptionIamBinding_codec);
            break;
          }
          case 34: {
            pubsubSubscriptionIamMember_.AddEntriesFrom(ref input, _repeated_pubsubSubscriptionIamMember_codec);
            break;
          }
          case 42: {
            pubsubSubscriptionIamPolicy_.AddEntriesFrom(ref input, _repeated_pubsubSubscriptionIamPolicy_codec);
            break;
          }
          case 50: {
            if (pubsubTopic_ == null) {
              PubsubTopic = new global::Oak9.Tython.Gcp.Pubsub.PubsubTopic();
            }
            input.ReadMessage(PubsubTopic);
            break;
          }
          case 58: {
            pubsubTopicIamBinding_.AddEntriesFrom(ref input, _repeated_pubsubTopicIamBinding_codec);
            break;
          }
          case 66: {
            pubsubTopicIamMember_.AddEntriesFrom(ref input, _repeated_pubsubTopicIamMember_codec);
            break;
          }
          case 74: {
            pubsubTopicIamPolicy_.AddEntriesFrom(ref input, _repeated_pubsubTopicIamPolicy_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code